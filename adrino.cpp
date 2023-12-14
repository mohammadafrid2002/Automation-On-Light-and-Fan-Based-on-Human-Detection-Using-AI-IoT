const int ledPin = D7;  // Pin connected to the LED (D7 on NodeMCU)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn off the LED
    }
  }
}
