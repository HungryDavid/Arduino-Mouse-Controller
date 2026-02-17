const int joyBtn = 7;
void setup() { 
    Serial.begin(115200); 
    Serial.setTimeout(1);
    pinMode(joyBtn, INPUT_PULLUP); 
}
void loop() {
    int x = analogRead(A0), y = analogRead(A1), btn = digitalRead(joyBtn);
    Serial.print(x); Serial.print(","); Serial.print(y); Serial.print(","); Serial.println(btn);
    delay(3);
}
