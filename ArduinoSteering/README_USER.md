# Arduino Steering Wheel - User Guide

## Quick Start

1. Copy this entire `ArduinoSteering` folder to your **Desktop**.
2. Connect your Arduino to the PC.
3. Double-click **`run.bat`**

The wheel should start working.

## Important Notes

- **Do not close** the Command Prompt window while using the wheel.
- If it doesn't connect:
  - Open `arduino_to_vjoy.py`
  - Change `SERIAL_PORT = "COM5"` to your actual port (check Device Manager).
- Calibrate the steering and pedals in your racing game.

## Controls

- **Steering** → Potentiometer
- **Accelerator** → W key / Axis
- **Brake** → S key / Axis
- **Clutch** → X key / Axis
- **Ignition Key**:
  - Pos 1 → 2: Turns on electronics (`Y`)
  - Pos 2 → 3: Cranks engine (`G`)
  - Pos 2 → 1: Shuts off car (`Y`)

Enjoy your drive!