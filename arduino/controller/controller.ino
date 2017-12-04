float percentage = 0;       // variable to store the data from the serial port
float pwmEmit = 0;
int ledPin=13;

void setup() {
 pinMode(ledPin,OUTPUT);    // declare the LED's pin as output
 Serial.begin(9600);        // connect to the serial port
}

void loop () {
  if (Serial.available()) { 
    percentage = Serial.readString().toFloat()/100.0;      // read the serial port
    pwmEmit = percentage * 255.0;
    
    //Serial.println("Percentage: "+(String)(percentage*100.0)+"%\t Val: "+pwmEmit);

    for(int x=0; x<percentage*100;x++){
      digitalWrite(ledPin, HIGH);
      delay(300);
      digitalWrite(ledPin, LOW);
      delay(300);
    }

  }
}
