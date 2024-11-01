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

//For BNO055
Adafruit_BNO055 myIMU = Adafruit_BNO055();

//radio setup
RF24 radio(9, 10);               //CE=D9 ,CSN=D10
RF24Network network(radio);      //Adding radio module to the network
const uint16_t this_node = 02;   //Giving address to this node
const uint16_t node00 = 00;      //Address of main node

//Defining variables
int t = 10; //delay time
float q0=0,q1=0,q2=0,q3=0,sinp;//for quaternions
struct ref_data {
  float y0,p0,r0;
 };
ref_data refdata;

void setup() {
  //BNO055 Setup
  Serial.begin(115200);
  myIMU.begin();
  delay(1000);
  myIMU.setExtCrystalUse(true);
  
  //RF module setup
  SPI.begin();
  radio.begin();
  network.begin(90, this_node);  //(channel=90, node address=this_node)
  radio.setDataRate(RF24_2MBPS);    
}

void loop(){
  network.update();
  RF24NetworkHeader header(node00);     // (Address where the data is going)

  imu::Quaternion quat=myIMU.getQuat();
  q0 = quat.w();
  q1 = quat.x();
  q2 = quat.y();
  q3 = quat.z();

  refdata.y0 = -(atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3)))*180/PI;
  sinp = 2*(q0*q2-q3*q1);
  if (abs(sinp) >=1){
    refdata.p0 = copysign(PI / 2, sinp)*180/PI;
  }
  if (abs(sinp) <1) {
    refdata.p0 = (asin(2*(q0*q2-q3*q1)))*180/PI;
  }
  refdata.r0 = -(atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2)))*180/PI;

    Serial.print("ypr ref");
    Serial.print(" , ");
    Serial.print(refdata.y0);
    Serial.print(" , ");
    Serial.print(refdata.p0);
    Serial.print(" , ");
    Serial.println(refdata.r0);

  //Sending data through network
  bool ok = network.write(header, &refdata, sizeof(ref_data)); // Sending data to receiver module (node 00)
  delay(t);
}
