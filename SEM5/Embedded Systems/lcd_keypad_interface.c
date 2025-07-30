#include <Keypad.h>
#include <LiquidCrystal.h>  // Use this instead of LiquidCrystal_I2C

// LCD: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, A0, A1, A2, A3);  // Adjust if needed

const byte ROWS = 4;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

int cursorCol = 0;

void setup() {
  Serial.begin(9600);  // Debug via Serial Monitor
  Serial.println("System starting...");

  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Press key:");
}

void loop() {
  char key = keypad.getKey();
  if (key) {
    Serial.print("Key pressed: ");
    Serial.println(key);

    lcd.setCursor(cursorCol, 1);
    lcd.print(key);
    cursorCol++;

    if (cursorCol >= 16) {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Press key:");
      cursorCol = 0;
    }
  }
}




/*
  === Arduino LCD + 4x3 Keypad Wiring Reference ===

  LCD Connections (16x2, Parallel Mode - 4-bit):
    RS  → D12
    E   → D11
    D4  → A0
    D5  → A1
    D6  → A2
    D7  → A3
    RW  → GND
    VSS → GND
    VDD → 5V
    VO  → Center of 10k Pot (ends to GND and 5V)
    LED+ (Pin 15) → 5V (or via 220Ω resistor)
    LED- (Pin 16) → GND

  Keypad Connections (4x3 Matrix, 7 Pins):
    Row 1 → D9
    Row 2 → D8
    Row 3 → D7
    Row 4 → D6
    Col 1 → D5
    Col 2 → D4
    Col 3 → D3

  Note:
    - Use a 10k potentiometer for contrast on LCD VO pin.
    - Ensure RW pin of LCD is grounded (GND).
    - Confirm pin order of keypad before connecting — wire from left to right or top to bottom based on your module.
*/
