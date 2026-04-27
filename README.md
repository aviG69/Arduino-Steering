# Arduino-Steering

A custom steering wheel interface using Arduino and vJoy.

## Components
- **final_steering/**: Arduino source code (.ino)
- **ArduinoSteering/**: Python bridge for data processing
- **vJoySerialFeeder/**: Windows utility and required drivers

## Setup
1. Upload the code in `final_steering/` to your Arduino.
2. Install the vJoy drivers included in the repository.
3. Use `vJoySerialFeeder.exe` to map the Arduino serial output to a virtual controller.
4. Calibrate the axis in your simulation software.

Built for low-latency steering input in racing simulations.

##Connections --
Accelerator(W) - 2/
Brake(S) - 3/
Clutch(X) - 4/
Potentiometer - A0/
