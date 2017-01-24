
int LED = 2;
int rod = 1;
int sensor = A0;

void setup() {
Serial.begin(9600);
pinMode (LED, OUTPUT);
pinMode (rod, OUTPUT);


void loop() {
digitalWrite(rod, HIGH);
delay(1000)
int sensorreading = analogRead(sensor);
Serial.printIn(sensorreading);

if(sensorreading <= 100)
{
  digitalWrite(LED, LOW);
}
else if (sensorreading >= 101)
 {
  digitalWrite(LED, HIGH);
 }
digitalWrite(rod, LOW);
delay(900000);
}
