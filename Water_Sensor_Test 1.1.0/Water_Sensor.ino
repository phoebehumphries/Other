void setup(){
 
Serial.begin(9600);
pinMode (LED, OUTPUT);
} 
void loop(){
 
Serial.print("Water level Sensor Value:");
Serial.println(analogRead(A0));
Serial.println
delay(10000);
 
}
