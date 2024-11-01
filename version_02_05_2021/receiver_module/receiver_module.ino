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
  float a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p;
};
incoming_Data incomingData;

struct ref_data {
  float y0,p0,r0;
};
ref_data refdata;

struct palm_data {
  float y1,p1,r1,y2,p2,r2,f0x,f0y,f1x,f1y,f2x,f2y,f3x,f3y,f4x,f4y;
 };
palm_data palmdata;

void setup() {
  Serial.begin(115200);

  int t = 10; //delay time
  SPI.begin();
  radio.begin();
  network.begin(90, this_node); //(channel=90, node address=this_node)
  radio.setDataRate(RF24_2MBPS);
}

void loop() {
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
    } 
    // receiving data from node02
    if (header.from_node == 2) {// from reference module
      refdata.y0 = incomingData.a;
      refdata.p0 = incomingData.b;
      refdata.r0 = incomingData.c; 
    }

    Serial.print(refdata.y0);
    Serial.print(" , ");
    Serial.print(refdata.p0);
    Serial.print(" , ");
    Serial.print(refdata.r0); 
    Serial.print(" , ");
    Serial.print(palmdata.y1);
    Serial.print(" , ");
    Serial.print(palmdata.p1);
    Serial.print(" , ");
    Serial.print(palmdata.r1);
    Serial.print(" , ");
    Serial.print(palmdata.y2);
    Serial.print(" , ");
    Serial.print(palmdata.p2);
    Serial.print(" , ");
    Serial.print(palmdata.r2);
    Serial.print(" , ");
    Serial.print(palmdata.f0x);
    Serial.print(" , ");
    Serial.print(palmdata.f0y);
    Serial.print(" , ");
    Serial.print(palmdata.f1x);
    Serial.print(" , ");
    Serial.print(palmdata.f1y);
    Serial.print(" , ");
    Serial.print(palmdata.f2x);
    Serial.print(" , ");
    Serial.print(palmdata.f2y);
    Serial.print(" , ");
    Serial.print(palmdata.f3x);
    Serial.print(" , ");
    Serial.print(palmdata.f3y);
    Serial.print(" , ");
    Serial.print(palmdata.f4x);
    Serial.print(" , ");
    Serial.print(palmdata.f4y);
    Serial.println("");
    delay(t);
  }
}
