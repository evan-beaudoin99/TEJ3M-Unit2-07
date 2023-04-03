/*
  Created by: Evan Beaudoin
  Created on: March 2023
  Uses the HC-SR04 distance sensor to detect when the distance is
  less than 10 to move a servo
*/


#include <Servo.h>

Servo servo;

const int TRIGPIN = 9;
const int ECHOPIN = 8;

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(TRIGPIN,  OUTPUT);
  pinMode(ECHOPIN, INPUT);
  
  servo.attach(7);
  servo.write(0);
  delay(2000);
 
}
void  loop() {
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  
  duration = pulseIn(ECHOPIN, HIGH);
  distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);

  if (distance < 10)
  {
    servo.write(180);
  }
  else
  {
    servo.write(0);
  }
}
