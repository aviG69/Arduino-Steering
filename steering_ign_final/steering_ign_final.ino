const int potPin = A0;   // Steering
const int gasPin = 3;    // Button 'W'
const int brakePin = 4;  // Button 'S'
const int extraPin = 5;  // Button 'X'
const int ignPin = 6;    // Ignition 'Y'
const int crankPin = 7;  // Crank 'G'

// Timer variables for non-blocking execution
unsigned long previousMillis = 0;
const long interval = 10; // Transmit data every 10 milliseconds (100Hz refresh rate)

// Debounce arrays to clean up mechanical switch noise
const int numButtons = 5;
int buttonPins[numButtons] = {gasPin, brakePin, extraPin, ignPin, crankPin};
int currentStates[numButtons] = {0, 0, 0, 0, 0};
int lastRawStates[numButtons] = {0, 0, 0, 0, 0};
unsigned long lastDebounceTime[numButtons] = {0, 0, 0, 0, 0};
const unsigned long debounceDelay = 15; // Ignore changes shorter than 15ms

void setup() {
  Serial.begin(115200); 
  
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  unsigned long currentMillis = millis();

  // 1. Read and Debounce all physical switches
  for (int i = 0; i < numButtons; i++) {
    int rawState = (digitalRead(buttonPins[i]) == LOW) ? 1 : 0;
    
    // If the switch physically moved, reset its debounce timer
    if (rawState != lastRawStates[i]) {
      lastDebounceTime[i] = currentMillis;
    }
    
    // If the state has been stable longer than the delay, lock it in
    if ((currentMillis - lastDebounceTime[i]) > debounceDelay) {
      currentStates[i] = rawState;
    }
    
    lastRawStates[i] = rawState; // Save for next loop
  }

  // 2. Transmit data exactly every 10ms (without freezing the board)
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    int steering = analogRead(potPin);
    int gas = currentStates[0];
    int brake = currentStates[1];
    int extra = currentStates[2];
    int rawIgn = currentStates[3];
    int rawCrank = currentStates[4];

    // Ignition overlap logic masking
    int ignOut = 0;
    int crankOut = 0;
    if (rawCrank == 1) {
      ignOut = 0;      
      crankOut = 1;    
    } else if (rawIgn == 1) {
      ignOut = 1;      
      crankOut = 0;    
    }

    // Wrap data in < > brackets to guarantee clean packet reading
    Serial.print("<");
    Serial.print(steering); Serial.print(",");
    Serial.print(gas); Serial.print(",");
    Serial.print(brake); Serial.print(",");
    Serial.print(extra); Serial.print(",");
    Serial.print(ignOut); Serial.print(",");
    Serial.print(crankOut);
    Serial.println(">");
  }
}