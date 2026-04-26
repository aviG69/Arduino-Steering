import serial
import pyvjoy
import pydirectinput
import time

SERIAL_PORT = "COM5" 
# Lower factor = smoother but more "lag". 0.15 is a sweet spot.
SMOOTHING_FACTOR = 0.15 

try:
    j = pyvjoy.VJoyDevice(1)
    ser = serial.Serial(SERIAL_PORT, 9600, timeout=0.05)
    print(f"--- FINAL STABLE BUILD ACTIVE ON {SERIAL_PORT} ---")
except Exception as e:
    print(f"Connection Error: {e}")
    exit()

key_map = {'w': False, 's': False, 'x': False}
current_smoothed_x = 16384 

def press_logic(key, is_pressed):
    if is_pressed and not key_map[key]:
        pydirectinput.keyDown(key)
        key_map[key] = True
    elif not is_pressed and key_map[key]:
        pydirectinput.keyUp(key)
        key_map[key] = False

while True:
    try:
        raw_line = ser.readline()
        if not raw_line: continue
        line = raw_line.decode('utf-8', errors='ignore').strip()
        
        if "," in line:
            parts = line.split(",")
            if len(parts) == 4:
                raw_val = int(parts[0])
                
                # Snap-to-center logic: if it's really close to middle, make it perfect
                if 505 < raw_val < 520:
                    target_x = 16384
                else:
                    target_x = 32767 - int(raw_val * 32767 / 1023)
                
                # Exponential Moving Average for ultra-smoothness
                current_smoothed_x = (target_x * SMOOTHING_FACTOR) + (current_smoothed_x * (1 - SMOOTHING_FACTOR))
                
                final_x = int(current_smoothed_x)
                j.set_axis(pyvjoy.HID_USAGE_X, final_x)

                # Keyboard Keys
                press_logic('w', parts[1] == "1")
                press_logic('s', parts[2] == "1")
                press_logic('x', parts[3] == "1")

                print(f"Steer: {final_x:5} | W:{parts[1]} S:{parts[2]} X:{parts[3]}", end='\r')
    except:
        ser.reset_input_buffer()
        continue