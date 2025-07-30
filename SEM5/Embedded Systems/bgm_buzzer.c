const int buzzer = 8;

#define C4  262
#define Cs4 277
#define D4  294
#define Ds4 311
#define E4  330
#define F4  349
#define Fs4 370
#define G4  392
#define Gs4 415
#define A4  440
#define As4 466
#define B4  494

// Simplified villain theme inspired melody (minor, tense intervals)
int melody[] = {
  A4, G4, Fs4, G4, A4, G4, Fs4, E4,
  D4, Cs4, D4, E4, Fs4, G4, Fs4, E4,
  D4, Cs4, B4, Cs4, D4, E4, Fs4, G4,
  Fs4, E4, D4, Cs4, B4
};

// Durations (ms) - with suspenseful pauses
int durations[] = {
  400, 300, 200, 300, 400, 300, 200, 600,
  300, 300, 200, 300, 400, 400, 300, 600,
  300, 300, 300, 300, 300, 400, 400, 400,
  300, 300, 400, 400, 700
};

void setup() {
  pinMode(buzzer, OUTPUT);
  int notes = sizeof(melody)/sizeof(melody[0]);

  for (int i = 0; i < notes; i++) {
    tone(buzzer, melody[i], durations[i]);
    delay(durations[i] * 1.2);  // slightly longer pause for tension
    noTone(buzzer);
  }
}

void loop() {
  // Play once
}
