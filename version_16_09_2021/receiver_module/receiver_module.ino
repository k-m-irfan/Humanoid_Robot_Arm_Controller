//Libraries required for RF Module
#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>

//radio setup
RF24 radio(9, 10);               // nRF24L01 CE=D9 ,CSN=D10
RF24Network network(radio);      // Adding radio module to the network
const uint16_t this_node = 00;   // Giving an address to this module(node)

//Defining variables
int t = 10; //delay time
struct incoming_Data{
  float a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q;
};
incoming_Data incomingData;

struct ref_data {
  float y0,p0,r0;
};
ref_data refdata;

struct palm_data {
  float y1,p1,r1,y2,p2,r2,f0x,f0y,f1x,f1y,f2x,f2y,f3x,f3y,f4x,f4y,delay1;
 };
palm_data palmdata;

//defining variables for IMU1-axis
struct k0 { //fron axis
  float x,y,z;
};
k0 k0;
struct s0 { //side axis
  float x,y,z;
};
s0 s0;
struct u0 { //up axis
  float x,y,z;
};
u0 u0;

//defining variables for IMU1-axis
struct k1 { //front axis
  float x,y,z;
};
k1 k1;
struct s1 { //side axis
  float x,y,z;
};
s1 s1;
struct u1 { //up axis
  float x,y,z;
};
u1 u1;

//defining variables for IMU1-axis
struct k2 { //front axis
  float x,y,z;
};
k2 k2;
struct s2 { //side axis
  float x,y,z;
};
s2 s2;
struct u2 { //up axis
  float x,y,z;
};
u2 u2;
struct ref1 { //reference1 axis
  float x,y,z;
};
ref1 ref1;
struct ref2 { //reference2 axis
  float x,y,z;
};
ref2 ref2;

//Variables for yaw, pitch and roll for all three IMUs
float y0,p0,r0,y1,p1,r1,y2,p2,r2;
//Variables for arm joint angles
float a,b,c,d,e,fx,fy;
//Variables for finger angles
float f0x,f0y,f1x,f1y,f2x,f2y,f3x,f3y,f4x,f4y;
//Reference axis for the upper arm rotation

//--------------------------------------------------------------
//to count data per second 
  float ftime0 = micros();
  int frequency = 0;
//--------------------------------------------------------------
void setup() {
  Serial.begin(115200);

  int t = 0; //delay time
  SPI.begin();
  radio.begin();
  network.begin(90, this_node); //(channel=90, node address=this_node)
  radio.setDataRate(RF24_2MBPS);

}

void loop() {
  float time0 = micros();// for receiver calculation time
//----------------------------------------------------------------------  
//For data count per second
  float ftime = micros()-ftime0;
  if (ftime > 1000000){
    //Serial.println(frequency);// Uncomment to print the data frequency
    frequency = 0;
    ftime0=micros();    
  }
  frequency+=1;
//----------------------------------------------------------------------

  network.update();
  while ( network.available()==1) {         // 1 = data is available
    
    RF24NetworkHeader header;
    //network.read(header, &refdata, sizeof(ref_data)); // reading available data
    //network.read(header, &wristdata, sizeof(wrist_data));
    network.read(header, &incomingData, sizeof(incomingData));
        
    // receiving data from node01
    if (header.from_node == 1) {// from wrist module
      palmdata.y1 = incomingData.a;
      palmdata.p1 = incomingData.b;
      palmdata.r1 = incomingData.c;
      palmdata.y2 = incomingData.d;
      palmdata.p2 = incomingData.e;
      palmdata.r2 = incomingData.f;

      palmdata.f0x = incomingData.g-100;
      palmdata.f0y = incomingData.h;
      palmdata.f1x = incomingData.i+20;
      palmdata.f1y = incomingData.j;
      palmdata.f2x = incomingData.k+20;
      palmdata.f2y = incomingData.l;
      palmdata.f3x = incomingData.m+30;
      palmdata.f3y = incomingData.n;
      palmdata.f4x = incomingData.o;
      palmdata.f4y = incomingData.p;
      palmdata.delay1 = incomingData.q;//delay from palm module
    } 
    // receiving data from node02
    if (header.from_node == 2) {// from reference module
      refdata.y0 = incomingData.a;
      refdata.p0 = incomingData.b;
      refdata.r0 = incomingData.c; 
    }

    //Assigning easy variable names for calculation and adding some offset adjustments
    float delay1 = palmdata.delay1;//delay from palm module
    
    y0 = (refdata.y0);
    p0 = (refdata.p0);
    r0 = (refdata.r0);

    y1 = (palmdata.y1);
    p1 = (palmdata.p1);
    r1 = (palmdata.r1);
    
    y2 = (palmdata.y2);
    p2 = (palmdata.p2);
    r2 = (palmdata.r2);

    //Finding axis vectors---------------------------------------------------
    //for IMU0 (Upper Arm)
    u0.x = sin(radians(y0-90))*sin(radians(r0))+cos(radians(y0-90))*sin(radians(p0))*cos(radians(r0));//up
    u0.y = cos(radians(p0))*cos(radians(r0));
    u0.z = -cos(radians(y0-90))*sin(radians(r0))+sin(radians(y0-90))*sin(radians(p0))*cos(radians(r0));

    k0.x = -sin(radians(y0+90))*cos(radians(r0))+cos(radians(y0+90))*sin(radians(p0))*sin(radians(r0));//k
    k0.y = -cos(radians(p0))*sin(radians(r0));
    k0.z = cos(radians(y0+90))*cos(radians(r0))+sin(radians(y0+90))*sin(radians(p0))*sin(radians(r0));

    s0.x = cos(radians(y0-90))*cos(radians(p0));//side
    s0.y = -sin(radians(p0));
    s0.z = sin(radians(y0-90))*cos(radians(p0));

    //for IMU1 (Forearm)
    u1.x = sin(radians(y1-90))*sin(radians(r1))+cos(radians(y1-90))*sin(radians(p1))*cos(radians(r1));//up
    u1.y = cos(radians(p1))*cos(radians(r1));
    u1.z = -cos(radians(y1-90))*sin(radians(r1))+sin(radians(y1-90))*sin(radians(p1))*cos(radians(r1));

    s1.x = sin(radians(y1+90))*cos(radians(r1))-cos(radians(y1+90))*sin(radians(p1))*sin(radians(r1));//side
    s1.y = cos(radians(p1))*sin(radians(r1));
    s1.z = -cos(radians(y1+90))*cos(radians(r1))-sin(radians(y1+90))*sin(radians(p1))*sin(radians(r1));

    k1.x = cos(radians(y1-90))*cos(radians(p1));//k
    k1.y = -sin(radians(p1));
    k1.z = sin(radians(y1-90))*cos(radians(p1));    

    //for IMU2 (Palm)
    u2.x = sin(radians(y2-90))*sin(radians(r2))+cos(radians(y2-90))*sin(radians(p2))*cos(radians(r2));//up
    u2.y = cos(radians(p2))*cos(radians(r2));
    u2.z = -cos(radians(y2-90))*sin(radians(r2))+sin(radians(y2-90))*sin(radians(p2))*cos(radians(r2));

    s2.x = sin(radians(y2+90))*cos(radians(r2))-cos(radians(y2+90))*sin(radians(p2))*sin(radians(r2));//side
    s2.y = cos(radians(p2))*sin(radians(r2));
    s2.z = -cos(radians(y2+90))*cos(radians(r2))-sin(radians(y2+90))*sin(radians(p2))*sin(radians(r2));

    k2.x = cos(radians(y2-90))*cos(radians(p2));//k
    k2.y = -sin(radians(p2));
    k2.z = sin(radians(y2-90))*cos(radians(p2)); 

    // Getting joint angles
    
    // Shoulder rotation angle (a)
    a = -degrees(atan2(k0.y,k0.z))-90;
    
    // Shoulder hinge angle (b)
    b = degrees(atan2(k0.x,sqrt(k0.y*k0.y+k0.z*k0.z)));
    
    // Upper arm twist (c)
    //reference axis-1 (ref1) perpendicular with k0_yz and global x axis
    //(0, k0.y, k0.z)
    //(1, 0,    0)
    ref1.x = 0;
    ref1.y = k0.z; 
    ref1.z = -k0.y;
    //reference axis-2 (ref2) perpendicular with k0 and k1 axis
    //(k0.x, k0.y, k0.z)
    //(k1.x, k1.y, k1.z)
    ref2.x = k0.y*k1.z-k1.y*k0.z;
    ref2.y = -(k0.x*k1.z-k1.x*k0.z);
    ref2.z = k0.x*k1.y-k1.x*k0.y;
    //Angle (c) ref1 ref2
    c = -degrees(acos((ref1.x*ref2.x+ref1.y*ref2.y+ref1.z*ref2.z)/(sqrt(ref1.x*ref1.x+ref1.y*ref1.y+ref1.z*ref1.z)*sqrt(ref2.x*ref2.x+ref2.y*ref2.y+ref2.z*ref2.z))))+90;
    
    // Elbow joint angle (d) k0 k1
    d = degrees(acos((k0.x*k1.x+k0.y*k1.y+k0.z*k1.z)/(sqrt(k0.x*k0.x+k0.y*k0.y+k0.z*k0.z)*sqrt(k1.x*k1.x+k1.y*k1.y+k1.z*k1.z))));
    
    // Wrist rotation (e)
    e = -(90-degrees(acos((s1.x*u0.x+s1.y*u0.y+s1.z*u0.z)/(sqrt(s1.x*s1.x+s1.y*s1.y+s1.z*s1.z)*sqrt(u0.x*u0.x+u0.y*u0.y+u0.z*u0.z)))));
    
    // Wrist pitch (fx) k2 u1
    fx = 90-degrees(acos((k2.x*u1.x+k2.y*u1.y+k2.z*u1.z)/(sqrt(k2.x*k2.x+k2.y*k2.y+k2.z*k2.z)*sqrt(u1.x*u1.x+u1.y*u1.y+u1.z*u1.z))));
    
    // Wrist yaw (fy) k2 s1
    fy = 90-degrees(acos((k2.x*s1.x+k2.y*s1.y+k2.z*s1.z)/(sqrt(k2.x*k2.x+k2.y*k2.y+k2.z*k2.z)*sqrt(s1.x*s1.x+s1.y*s1.y+s1.z*s1.z))));
            
    // Getting angles for all the fingers and adding adjustments
    f0y = palmdata.f0x+60;
    f0x = palmdata.f0y+10;
    f1y = palmdata.f1x;
    f1x = palmdata.f1y;
    f2y = palmdata.f2x;
    f2x = palmdata.f2y+10;
    f3y = palmdata.f3x;
    f3x = palmdata.f3y;
    f4y = palmdata.f4x*2;
    f4x = palmdata.f4y; 

    /*Serial.print(y0);
    Serial.print(" , ");
    Serial.print(p0);
    Serial.print(" , ");
    Serial.print(r0); 
    Serial.print(" , ");
    Serial.print(y1);
    Serial.print(" , ");
    Serial.print(p1);
    Serial.print(" , ");
    Serial.print(r1);
    Serial.print(" , ");
    Serial.print(y2);
    Serial.print(" , ");
    Serial.print(p2);
    Serial.print(" , ");
    Serial.print(r2);
    Serial.print(" , ");*/
//-----------------------------------------------------------    
    Serial.print(a);
    Serial.print(" , ");
    Serial.print(b);
    Serial.print(" , ");
    Serial.print(c);
    Serial.print(" , ");
    Serial.print(d);
    Serial.print(" , ");
    Serial.print(e);
    Serial.print(" , ");
    Serial.print(fx);
    Serial.print(" , ");
    Serial.print(fy);
    Serial.print(" , ");
    Serial.print(f0x);
    Serial.print(" , ");
    Serial.print(f0y);
    Serial.print(" , ");
    Serial.print(f1x);
    Serial.print(" , ");
    Serial.print(f1y);
    Serial.print(" , ");
    Serial.print(f2x);
    Serial.print(" , ");
    Serial.print(f2y);
    Serial.print(" , ");
    Serial.print(f3x);
    Serial.print(" , ");
    Serial.print(f3y);
    Serial.print(" , ");
    Serial.print(f4x);
    Serial.print(" , ");
    Serial.print(f4y);
//---------------------------------------------    
    
    /*Serial.print(k0.x);
    Serial.print(" , ");
    Serial.print(k0.y);
    Serial.print(" , ");
    Serial.print(k0.z);
    Serial.print(" , ");
    Serial.print(s0.x);
    Serial.print(" , ");
    Serial.print(s0.y);
    Serial.print(" , ");
    Serial.print(s0.z);
    Serial.print(" , ");
    Serial.print(u0.x);
    Serial.print(" , ");
    Serial.print(u0.y);
    Serial.print(" , ");
    Serial.print(u0.z);
    Serial.print(" , ");
    
    Serial.print(k1.x);
    Serial.print(" , ");
    Serial.print(k1.y);
    Serial.print(" , ");
    Serial.print(k1.z);
    Serial.print(" , ");
    Serial.print(s1.x);
    Serial.print(" , ");
    Serial.print(s1.y);
    Serial.print(" , ");
    Serial.print(s1.z);
    Serial.print(" , ");
    Serial.print(u1.x);
    Serial.print(" , ");
    Serial.print(u1.y);
    Serial.print(" , ");
    Serial.print(u1.z);
    Serial.print(" , ");

    Serial.print(k2.x);
    Serial.print(" , ");
    Serial.print(k2.y);
    Serial.print(" , ");
    Serial.print(k2.z);
    Serial.print(" , ");
    Serial.print(s2.x);
    Serial.print(" , ");
    Serial.print(s2.y);
    Serial.print(" , ");
    Serial.print(s2.z);
    Serial.print(" , ");
    Serial.print(u2.x);
    Serial.print(" , ");
    Serial.print(u2.y);
    Serial.print(" , ");
    Serial.print(u2.z);*/
//-------------------------------------------------------------------
//for overall response delay
//    float delay3 = micros()-time0;
//    Serial.print(" , ");
//    Serial.print(delay1+delay3);
//-------------------------------------------------------------------    
    Serial.println("");
    delay(t);
  }
}
