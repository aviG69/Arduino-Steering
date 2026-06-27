@echo off
echo ========================================
echo   Arduino Steering Wheel Controller
echo ========================================
echo.

cd /d "%~dp0"

echo Installing dependencies (if needed)...
python -m pip install -r requirements.txt

echo.
echo ========================================
echo Starting Steering Wheel...
echo ========================================
echo.
echo ** DO NOT CLOSE THIS WINDOW **
echo The steering wheel needs this window open to work.
echo.

python arduino_to_vjoy.py

echo.
echo Steering controller stopped.
pause