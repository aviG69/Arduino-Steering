@echo off
echo ========================================
echo   Arduino Steering Wheel Controller
echo ========================================
echo.

cd /d "%~dp0"

echo Installing dependencies...
python -m pip install -r requirements.txt

echo.
echo Running the steering controller...
python arduino_to_vjoy.py

pause