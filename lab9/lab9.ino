int ledPins[] = {43, 44, 45, 46};
int btnPins[] = {38,39,40,41}; 
int numItems = 4;

bool ledStates[] = {LOW, LOW, LOW, LOW};
bool lastBtnStates[] = {LOW, LOW, LOW, LOW};

void setup() {
  for (int i = 0; i < numItems; i++) {
    pinMode(ledPins[i], OUTPUT);
    pinMode(btnPins[i], INPUT);
  }
}
/*
void loop() {
  digitalWrite(43, HIGH); 
  delay(1000);           

  digitalWrite(43, LOW);  
  delay(1000);            
}
*/

void loop() {
  for (int i = 0; i < numItems; i++) {
    bool currentBtnState = digitalRead(btnPins[i]);

    if (currentBtnState == HIGH && lastBtnStates[i] == LOW) {

      ledStates[i] = !ledStates[i];
      digitalWrite(ledPins[i], ledStates[i]);

      delay(50);
    }

    lastBtnStates[i] = currentBtnState;
  }
}

