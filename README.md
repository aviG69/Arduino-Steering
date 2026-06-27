# Arduino Steering Wheel Controller

**A low-latency custom steering wheel with realistic ignition key support** for racing simulators. Built with Arduino and vJoy.

![Project Photo](images/steering_wheel.jpg)

## Overview

This project turns a simple Arduino setup into a fully functional USB steering wheel + pedals with a **realistic ignition key switch**. Perfect for games like **Assetto Corsa, iRacing, BeamNG, MyWinterCar**, etc.

## Features

- Smooth analog steering with EMA filtering
- Digital pedals (Accelerator, Brake, Clutch)
- **Realistic Ignition Switch** (UNO MINDA 7606) with physical key
- Low-latency serial communication
- Easy launcher (`run.bat`)

## Ignition Switch Behavior

The ignition key works as follows:

- **Position 1 → Position 2**: Presses `Y` once (turns on electronics / accessories)
- **Position 2 → Position 3** (Crank, spring-loaded): Holds `G` (starter)
- **Back to Position 2**: No additional key press
- **Position 2 → Position 1**: Presses `Y` again (shuts down the car)

This gives a very immersive, real-car-like ignition experience.

## Tech Stack

- **Microcontroller**: Arduino Uno / Nano
- **Firmware**: C++ (Arduino)
- **Bridge**: Python (pyserial + pyvjoy + pydirectinput)
- **Virtual Joystick**: vJoy

## Hardware

**Full Schematic**: [View Schematic](hardware/schematic.png)

**Pin Connections:**

| Component                    | Arduino Pin | Notes |
|-----------------------------|-------------|-------|
| Steering Potentiometer      | A0          | 10kΩ |
| Accelerator (W)             | D3          | |
| Brake (S)                   | D4          | |
| Clutch (X)                  | D5          | |
| Ignition Switch             | D6, D7      | Multi-position key switch |

## Easy Setup

1. Copy the entire **`ArduinoSteering`** folder to your **Desktop**.
2. Double-click **`run.bat`** inside that folder.
3. Connect your Arduino and calibrate in your simulator.

> **Important**: Keep the Command Prompt window open while using the wheel.

## Repository Structure

- `ArduinoSteering/` → Folder to copy to Desktop (run from here)
- `firmware/` → Arduino code
- `hardware/` → Schematic + documentation
- `images/` → Photos and demos
- `docs/` → Extra documentation
- `archive/`→ Old code and firmware

## Port Configuration

The Python script defaults to `COM5`. If your Arduino is connected to a different port:

1. Open `arduino_to_vjoy.py`
2. Change this line:
   ```python
   SERIAL_PORT = "COM5"