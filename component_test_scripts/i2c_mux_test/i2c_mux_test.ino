#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"
#include "Wire.h"

MPU6050 mpu;
MPU6050 mpu2;

#define MUX_Address 0x70

// I2C bus select
void selectBus(uint8_t i) {
  if (i > 7) return;
  Wire.beginTransmission(MUX_Address);
  Wire.write(1 << i);
  Wire.endTransmission();
}

uint8_t mpuIntStatus,mpuIntStatus2;     // holds actual interrupt status byte from MPU
uint8_t devStatus,devStatus2;           // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize,packetSize2;        // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount,fifoCount2;          // count of all bytes currently in FIFO
uint8_t fifoBuffer[64],fifoBuffer2[64]; // FIFO storage buffer

Quaternion q,q2;              // [w, x, y, z]
VectorInt16 aa,aa2;           // [x, y, z]
VectorInt16 aaReal,aaReal2;   // [x, y, z]
VectorInt16 aaWorld,aaWorld2; // [x, y, z]
VectorFloat gravity,gravity2; // [x, y, z]
float ypr[3];                 // [yaw, pitch, roll]
float ypr2[3];
float y,p,r,y2,p2,r2;

void setup() {
    Wire.begin();
    Serial.begin(115200);
    selectBus(0);
    mpu.initialize();
    devStatus = mpu.dmpInitialize();

    // supply your own gyro offsets here, scaled for min sensitivity
    mpu.setXGyroOffset(220);
    mpu.setYGyroOffset(76);
    mpu.setZGyroOffset(-85);
    mpu.setZAccelOffset(1788); // 1688 factory default for my test chip

    if (devStatus == 0) {
        // Calibration Time: generate offsets and calibrate our MPU6050
        mpu.CalibrateAccel(6);
        mpu.CalibrateGyro(6);
        mpu.PrintActiveOffsets();
        mpu.setDMPEnabled(true);
        Serial.println("DMP Success");
        mpuIntStatus = mpu.getIntStatus();
        packetSize = mpu.dmpGetFIFOPacketSize();
    } else {
        Serial.println("DMP Failed");
    }

    selectBus(1);
    mpu2.initialize();
    devStatus2 = mpu2.dmpInitialize();

    // supply your own gyro offsets here, scaled for min sensitivity
    mpu2.setXGyroOffset(220);
    mpu2.setYGyroOffset(76);
    mpu2.setZGyroOffset(-85);
    mpu2.setZAccelOffset(1788); // 1688 factory default for my test chip

    // make sure it worked (returns 0 if so)
    if (devStatus2 == 0) {
        // Calibration Time: generate offsets and calibrate our MPU6050
        mpu2.CalibrateAccel(6);
        mpu2.CalibrateGyro(6);
        mpu2.PrintActiveOffsets();
        mpu2.setDMPEnabled(true);
        Serial.println("DMP Success");
        mpuIntStatus2 = mpu2.getIntStatus();
        packetSize2 = mpu2.dmpGetFIFOPacketSize();
    } else {
        Serial.println("DMP Failed");
    }
}

void loop() {
    selectBus(1);
    if (mpu2.dmpGetCurrentFIFOPacket(fifoBuffer2)) { // Get the Latest packet 
//            mpu2.dmpGetQuaternion(&q2, fifoBuffer2);
//            Serial.print("quat\t");
//            Serial.print(q2.w);
//            Serial.print("\t");
//            Serial.print(q2.x);
//            Serial.print("\t");
//            Serial.print(q2.y);
//            Serial.print("\t");
//            Serial.println(q2.z);
            
            mpu2.dmpGetQuaternion(&q2, fifoBuffer2);
            mpu2.dmpGetGravity(&gravity2, &q2);
            mpu2.dmpGetYawPitchRoll(ypr2, &q2, &gravity2);
            y2 = ypr2[0]* 180/M_PI;
            p2 = ypr2[1]* 180/M_PI;
            r2 = ypr2[2]* 180/M_PI;
    }

    selectBus(0);
    if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) {
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetGravity(&gravity, &q);
            mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
            y = ypr[0]* 180/M_PI;
            p = ypr[1]* 180/M_PI;
            r = ypr[2]* 180/M_PI;
    }
    
Serial.print(y);
Serial.print("  ");
Serial.print(p);
Serial.print("  ");
Serial.print(r);
Serial.print("  |  ");
Serial.print(y2);
Serial.print("  ");
Serial.print(p2);
Serial.print("  ");
Serial.println(r2);
}