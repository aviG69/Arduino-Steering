const int potPin = A0;   // Steering
const int gasPin = 3;    // Button for 'W'
const int brakePin = 4;  // Button for 'S'
const int extraPin = 5;  // Button for 'X'

void setup() {
  Serial.begin(9600); 
  pinMode(gasPin, INPUT_PULLUP);
  pinMode(brakePin, INPUT_PULLUP);
  pinMode(extraPin, INPUT_PULLUP);
}

void loop() {
  int steering = analogRead(potPin);
  int gas = (digitalRead(gasPin) == LOW) ? 1 : 0;
  int brake = (digitalRead(brakePin) == LOW) ? 1 : 0;
  int extra = (digitalRead(extraPin) == LOW) ? 1 : 0;

  // Format: Steering,Gas,Brake,Extra
  Serial.print(steering);
  Serial.print(",");
  Serial.print(gas);
  Serial.print(",");
  Serial.print(brake);
  Serial.print(",");
  Serial.println(extra); 

  delay(10);
}