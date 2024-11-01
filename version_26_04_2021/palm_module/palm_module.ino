//Libraries required for BNO055 Sensor and calculations
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>

//Libraries required for RF Module
#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>

//For BNO055 x 2
Adafruit_BNO055 myIMU = Adafruit_BNO055(55,0x28);
Adafruit_BNO055 myIMU2 = Adafruit_BNO055(56,0x29);

//radio setup
RF24 radio(9, 10);               // CE=D9 ,CSN=D10
RF24Network network(radio);      // Adding radio module to the network
const uint16_t this_node = 01;   // Giving address to this node
const uint16_t node00 = 00;      // Address of main node

//Defining variables
int t = 10; //delay time
float q0=0,q1=0,q2=0,q3=0,sinp;//for quaternions
struct palm_data {
  float y1,p1,r1,y2,p2,r2;
 };
palm_data palmdata;

void setup() {
  //Setting up for analog mux channel select
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

  Serial.begin(115200);

  //RF module setup
  SPI.begin();
  radio.begin();
  network.begin(90, this_node);  //(channel=90, node address=this_node)
  radio.setDataRate(RF24_2MBPS);

  myIMU.begin();
  delay(500);
  myIMU.setExtCrystalUse(true);

  myIMU2.begin();
  delay(500);
  myIMU2.setExtCrystalUse(true);
  
}
void loop() {
  network.update();
  RF24NetworkHeader header(node00);     // (Address where the data is going)

  //Getting sensor data
  //-----------------------------------------------------------------------------

  imu::Quaternion quat=myIMU.getQuat();
  q0 = quat.w();
  q1 = quat.x();
  q2 = quat.y();
  q3 = quat.z();

    palmdata.y1 = -(atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3)))*180/PI;
    sinp = 2*(q0*q2-q3*q1);//To avoid singularity problem
  if (abs(sinp) >=1){
    palmdata.p1 = copysign(PI / 2, sinp)*180/PI;
  }
  if (abs(sinp) <1){
    palmdata.p1 = (asin(2*(q0*q2-q3*q1)))*180/PI;
  }
    palmdata.r1 = -(atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2)))*180/PI;

  imu::Quaternion quat2=myIMU2.getQuat();
  q0 = quat2.w();
  q1 = quat2.x();
  q2 = quat2.y();
  q3 = quat2.z();

    palmdata.y2 = -(atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3)))*180/PI;
    sinp = 2*(q0*q2-q3*q1);//To avoid singularity problem
  if (abs(sinp) >=1){
    palmdata.p2 = copysign(PI / 2, sinp)*180/PI;
  }
  if (abs(sinp) <1) {
    palmdata.p2 = (asin(2*(q0*q2-q3*q1)))*180/PI;
  }
    palmdata.r2 = -(atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2)))*180/PI;

    Serial.print("ypr wrist");
    Serial.print(" , ");
    Serial.print(palmdata.y1);
    Serial.print(" , ");
    Serial.print(palmdata.p1);
    Serial.print(" , ");
    Serial.print(palmdata.r1);
    Serial.print(" , ");
    Serial.print("ypr palm");
    Serial.print(" , ");
    Serial.print(palmdata.y2);
    Serial.print(" , ");
    Serial.print(palmdata.p2);
    Serial.print(" , ");
    Serial.print(palmdata.r2);
    Serial.println(" ");

  //-----------------------------------------------------------------------------
  //Sending data through network
  bool ok = network.write(header, &palmdata, sizeof(palm_data));
}


//custom function to select MUX channel------------------------------------------
void select_channel(int i){
  if (i==0){ // for channel 0
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    digitalWrite(4, LOW);
    digitalWrite(3, LOW);
    //Serial.println("channel 0");
  }
  if (i==1){ // for channel 1
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    digitalWrite(4, LOW);
    digitalWrite(3, HIGH);
    //Serial.println("channel 1");
  }
  if (i==2){ // for channel 2
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(3, LOW);
    //Serial.println("channel 2");
  }
  if (i==3){ // for channel 3
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(3, HIGH);
    //Serial.println("channel 3");
  }
  if (i==4){ // for channel 4
    digitalWrite(6, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(3, LOW);
    //Serial.println("channel 4");
  }
  if (i==5){ // for channel 5
    digitalWrite(6, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(3, HIGH);
    //Serial.println("channel 5");
  }
  if (i==6){ // for channel 6
    digitalWrite(6, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(4, HIGH);
    digitalWrite(3, LOW);
    //Serial.println("channel 6");
  }

}
