float percentage = 0;       // variable to store the data from the serial port
float pwmEmit = 0;
int ledPin=3;
int ledPin2=6;
int ledPin3=9;
int ledPin4=11;

void setup() {
 pinMode(ledPin,OUTPUT);    // declare the LED's pin as output
 pinMode(ledPin2,OUTPUT);    // declare the LED's pin as output
 pinMode(ledPin3,OUTPUT);    // declare the LED's pin as output
 pinMode(ledPin4,OUTPUT);    // declare the LED's pin as output
 
 Serial.begin(9600);        // connect to the serial port
}

void loop () {
  if (Serial.available()) { 
    percentage = Serial.readString().toFloat()/100.0;      // read the serial port
    pwmEmit = percentage * 255.0;
    
    //Serial.println("Percentage: "+(String)(percentage*100.0)+"%\t Val: "+pwmEmit);

    analogWrite(ledPin, pwmEmit);
    analogWrite(ledPin2, pwmEmit);
    analogWrite(ledPin3, pwmEmit);
    analogWrite(ledPin4, pwmEmit);
    

  }
}
