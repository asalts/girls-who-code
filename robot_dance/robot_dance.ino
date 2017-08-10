
#include <Servo.h>

Servo leftServo;  // create servo object to control a servo
Servo rightServo;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  leftServo.attach(12);  // attaches the servo on pin 9 to the servo object
  rightServo.attach(13);

 pinMode(1, OUTPUT);
 pinMode(2, OUTPUT);
 pinMode(3, OUTPUT);
}

//choreo goes here
void loop() {

dance();

 digitalWrite(1, HIGH);
 digitalWrite(2, HIGH);
 digitalWrite(3, HIGH);
 delay(681);              
 digitalWrite(1, LOW);
 digitalWrite(2, LOW);
 digitalWrite(3, LOW);
 delay(681); 

}

void dance() {
 //sway
right1();
delay(300);
forward();
delay(2000);
left1();
delay(300);
forward();
delay(2000);
right1();
delay(300);
forward();
delay(2000);
left1();
delay(300);
forward();
delay(2000);
//full circle
reverse();
delay(1000);
right1();
delay(500);
forward();
delay(1000);
left1();
delay(3000);
//sway pt2
right1();
delay(500);
forward();
delay(3000);
left1();
delay(500);
forward();
delay(3000);
right1();
delay(500);
forward();
delay(3000);
left1();
delay(500);
forward();
delay(3000);
//half circle
right1();
delay(50);
forward();
delay(1000);
right1();
delay(50);
forward();
delay(1000);
right1();
delay(50);
forward();
delay(1000);
reverse();
delay(1000); 
}

//these are defined functions
void forward() {
leftServo.write(0);
rightServo.write(180);
}

void reverse() {
leftServo.write(180);
rightServo.write(0);
}

void pause() {
leftServo.writeMicroseconds(1500);
rightServo.writeMicroseconds(1500);
}

void right() {
leftServo.write(180);
rightServo.write(180);
}

void right1() {
leftServo.write(135);
rightServo.write(135);
}

void left() {
leftServo.write(0);
rightServo.write(0);
}

void left1() {
leftServo.write(45);
rightServo.write(45);
}

