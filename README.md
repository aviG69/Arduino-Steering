# Arduino Steering Wheel Controller

**A low-latency custom steering wheel for racing simulators** built with Arduino and vJoy.

![Project Photo](images/steering_wheel.jpg)
*(Add a good photo or GIF here)*

## Overview

This project turns a simple Arduino setup (potentiometer + buttons) into a fully functional USB steering wheel + pedals for games like **Assetto Corsa, iRacing, Dirt Rally, BeamNG**, etc.

It features:
- Smooth analog steering with noise filtering
- Digital pedal inputs (Accelerator, Brake, Clutch)
- High update rate for responsive feel
- Python bridge for data processing and vJoy integration

## Features

- Real-time steering input via potentiometer
- EMA (Exponential Moving Average) filtering for smooth control
- Keyboard fallback support
- Easy calibration in simulation software
- Low-latency serial communication

## Tech Stack

- **Microcontroller**: Arduino Uno / Nano
- **Firmware**: C++ (Arduino)
- **Bridge**: Python (pyserial + pyvjoy + pydirectinput)
- **Virtual Joystick**: vJoy

## Hardware Connections

| Component          | Pin     |
|--------------------|---------|
| Potentiometer (Steering) | A0   |
| Accelerator (W)    | Pin 3   |
| Brake (S)          | Pin 4   |
| Clutch (X)         | Pin 5   |

**Full wiring diagram and BOM coming soon** (add them!)

## Setup Instructions

### 1. Arduino Firmware
1. Open `final_steering/final_steering.ino` (better to rename to `steering_controller.ino`)
2. Upload to your Arduino

### 2. Software Setup (Windows)

```bash
# Recommended: Create a virtual environment first
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt