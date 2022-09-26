#include "MPU6050_6Axis_MotionApps20.h"
#include "Wire.h"

MPU6050 mpu;
uint16_t packetSize;
uint16_t fifoCount;
uint8_t fifoBuffer[64]; // FIFO storage buffer
uint8_t mpuIntStatus;
Quaternion q;
VectorFloat gravity;
VectorInt16 gyro;
float ypr[3],y,p,r;

struct ref_data {
  float y;
  float p;
  float r;
 };
ref_data refdata;

void setup() {
  Serial.begin(115200);
  Serial.printf("here");
  Wire.begin();
  
  mpu.initialize();

  if (mpu.dmpInitialize() == 0){
    mpu.CalibrateAccel(6);
    mpu.CalibrateGyro(6);
    mpu.PrintActiveOffsets();
    mpu.setDMPEnabled(true);
    Serial.println(F("DMP ready!"));
    packetSize = mpu.dmpGetFIFOPacketSize();    
    }
    else{
      Serial.print("DMP failed!");
    }
      
}

void loop(){  
  mpuIntStatus = mpu.getIntStatus();
  fifoCount = mpu.getFIFOCount();
  if (mpuIntStatus & (0x01 << MPU6050_IMU::MPU6050_INTERRUPT_DMP_INT_BIT)){
    
    while(fifoCount >= packetSize){ 
      mpu.getFIFOBytes(fifoBuffer, packetSize);
      fifoCount -= packetSize;
      }

    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    mpu.dmpGetGyro(&gyro, fifoBuffer);

    refdata.y = asin(2*(q.x*q.y+q.z*q.w))*180/PI;
    refdata.p = -atan2(2*(q.y*q.w-q.x*q.z),1-2*(q.y*q.y+q.z*q.z))*180/PI;
    refdata.r = atan2(2*(q.x*q.w-q.y*q.z),1-2*(q.x*q.x+q.z*q.z))*180/PI;

    Serial.print("ypr ref");
    Serial.print("   ");
    Serial.print(refdata.y);
    Serial.print("   ");
    Serial.print(refdata.p);
    Serial.print("   ");
    Serial.println(refdata.r);

    }
}
