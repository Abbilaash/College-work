const int LED1 = A0;
const int LED2 = A1;

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  Serial.begin(9600);
  Serial.println("Type 'A' or 'B' in Serial Monitor:");
}

void loop() {
  if (Serial.available()) {
    char input = Serial.read();
    input = toupper(input); // Normalize to uppercase

    if (input == 'A') {
      digitalWrite(LED1, HIGH);
      Serial.println("LED1 ON (A0)");
    } 
    else if (input == 'B') {
      digitalWrite(LED2, HIGH);
      Serial.println("LED2 ON (A1)");
    }
  }
}


/*
A0, A1 with LED1 and LED2
*/
