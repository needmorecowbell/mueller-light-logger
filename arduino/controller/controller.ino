void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  String inputString = "";
}

void loop() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:

  }
}
