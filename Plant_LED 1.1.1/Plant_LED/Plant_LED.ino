
int LED = 3;
int LED = 2;
int LED = 1;
int rod = 1;
int sensor = A0;
//This is setting the pins to the correct LED's and sensor.

void setup() {
Serial.begin(9600);
//9600 is the number that is on the serial monitor
pinMode (LED, OUTPUT);
pinMode (rod, OUTPUT);
//This is setting the LED and rod as outputs, as they are giving data/stuff.

void loop() {
digitalWrite(rod, HIGH);
//rod is turned on
delay(1000)
//There is a delay after it is turned on (1 second)

int sensorreading = analogRead(sensor);
//This is creating sensorreading and setting it to the reading from the sensor.

              //Serial.printIn(sensorreading); (moving this into the loop.)
              //this prints the data to the monitor in a readable format.

if(sensorreading 50 >= 100)
//if the reading is equal/lower than a certain amount a different LED will turn on.
{
  Serial.print("The moisture level is: ");
  Serial.println(sensorreading);
  Serial.print("NEEDS WATER. NEEDS WATER. NEEDS WATER.");
  digitalWrite(LED, HIGH);

//If brightness is at either extreme of its value (either 0 or 255), then 

}

else if (sensorreading 101 >= 159);
{
  Serial.print("The moisture level is: ");
  Serial.println(sensorreading);
  Serial.print("PLEASE ADD WATER SOON. I'M GETTING DRY.");
  digitalWrite(LED,HIGH);
  
  
  }
}
//
else if (sensorreading >= 200)
 {
  digitalWrite(LED, LOW);
 }
digitalWrite(rod, LOW);
delay(10000); //10 seconds, final code will be either every hour or every 2 hours.
}
