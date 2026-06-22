import serial
import pyvjoy
import pydirectinput
import time
import sys

# Kill default lag
pydirectinput.PAUSE = 0.0

SERIAL_PORT = "COM5" 
BAUD_RATE = 115200
SMOOTHING_FACTOR = 0.15 

print("Attempting to connect to Sim Rig...")

# Enhanced connection handling
try:
    j = pyvjoy.VJoyDevice(1)
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.05)
    print(f"--- HARDENED BUILD ACTIVE ON {SERIAL_PORT} ---")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    print("Is the Arduino plugged in? Is the Arduino IDE Serial Monitor closed?")
    sys.exit()

key_map = {'w': False, 's': False, 'x': False, 'g': False}
current_smoothed_x = 16384 
prev_key_active = False

def press_logic(key, is_pressed):
    if is_pressed and not key_map[key]:
        pydirectinput.keyDown(key)
        key_map[key] = True
    elif not is_pressed and key_map[key]:
        pydirectinput.keyUp(key)
        key_map[key] = False

# Ensure clean start by wiping old data lingering in the USB buffer
ser.reset_input_buffer()

while True:
    try:
        # Save PC CPU overhead when no data is waiting
        if ser.in_waiting == 0:
            time.sleep(0.001)
            continue

        raw_line = ser.readline()
        if not raw_line: 
            continue
            
        line = raw_line.decode('utf-8', errors='ignore').strip()
        
        # STRICT DATA VALIDATION: Only accept packets formatted as <data>
        if line.startswith("<") and line.endswith(">"):
            # Strip the brackets before splitting
            clean_line = line[1:-1]
            parts = clean_line.split(",")
            
            # Ensure packet hasn't dropped any variables
            if len(parts) == 6:
                try:
                    # Convert to integers to catch any random letter corruption
                    raw_val = int(parts[0])
                    ign = int(parts[4])
                    crank = int(parts[5])
                except ValueError:
                    continue # Silently ignore corrupted frames

                # --- Steering Logic ---
                if 505 < raw_val < 520:
                    target_x = 16384
                else:
                    # Clamp constraints to avoid vJoy crashing from out-of-bounds math
                    target_x = max(0, min(32767, 32767 - int(raw_val * 32767 / 1023)))
                
                current_smoothed_x = (target_x * SMOOTHING_FACTOR) + (current_smoothed_x * (1 - SMOOTHING_FACTOR))
                final_x = int(current_smoothed_x)
                j.set_axis(pyvjoy.HID_USAGE_X, final_x)

                # --- Button Logic ---
                press_logic('w', parts[1] == "1")
                press_logic('s', parts[2] == "1")
                press_logic('x', parts[3] == "1")
                press_logic('g', crank == 1)

                # --- Ignition Toggle Logic ---
                current_key_active = (ign == 1 or crank == 1)
                if current_key_active != prev_key_active:
                    pydirectinput.keyDown('y')
                    pydirectinput.keyUp('y')
                    prev_key_active = current_key_active

                print(f"Steer: {final_x:5} | W:{parts[1]} S:{parts[2]} X:{parts[3]} Y:{1 if current_key_active else 0} G:{parts[5]}", end='\r')

    except KeyboardInterrupt:
        print("\nSafely disengaging virtual controller...")
        break
    except Exception as e:
        print(f"\nNon-fatal loop error caught: {e}")
        ser.reset_input_buffer()
        time.sleep(0.1)

# Cleanup
for k in key_map:
    pydirectinput.keyUp(k)
ser.close()
print("System Offline. Goodbye!")