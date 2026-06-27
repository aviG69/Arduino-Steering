# Arduino Steering Wheel Controller

**A low-latency custom steering wheel with realistic ignition key support** for racing simulators. Built with Arduino and vJoy.

![Project Photo](images/steering_wheel.jpg)

## Overview

This project turns a simple Arduino setup into a fully functional USB steering wheel + pedals with a **real ignition key switch**. Perfect for games like **Assetto Corsa, iRacing, BeamNG, MyWinterCar**, etc.

## Features

- Smooth analog steering with EMA filtering
- Digital pedals (Accelerator, Brake, Clutch)
- **Realistic Ignition Switch** (UNO MINDA 7606) with physical key
  - Simulates `Y` (Engine On) and `G` (Engine Off) keys
- Low-latency serial communication
- Easy-to-use launcher (`run.bat`)

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
| Ignition Switch             | D6, D7      | Key-operated |

**Bill of Materials**: [See BOM](hardware/BOM.md)

## Easy Setup (Recommended)

1. Copy the entire **`ArduinoSteering`** folder to your **Desktop**.
2. Double-click **`run.bat`** inside that folder.
3. Connect your Arduino and calibrate in your simulator.

> **Note**: Keep the Command Prompt window open while using the wheel.

### Manual Setup (Alternative)

```bash
cd ArduinoSteering
pip install -r requirements.txt
python arduino_to_vjoy.py