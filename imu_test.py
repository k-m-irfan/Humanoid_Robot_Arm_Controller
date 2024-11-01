from vpython import *
from time import *
import numpy as np
import math
import serial
ad=serial.Serial('com4',115200)
sleep(1)
scene.forward=vector(-1,-1,-1)

scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad

xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(lenght=4, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=1,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=2,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

bBoard=box(length=6,width=2,height=.2,opacity=.8,pos=vector(0,0,0,))
bn=box(length=1,width=.75,height=.1, pos=vector(-.5,.1+.05,0),color=color.blue)
nano=box(lenght=1.75,width=.6,height=.1,pos=vector(-2,.1+.05,0),color=color.green)
myObj=compound([bBoard,bn,nano])
while (True):
    try:
        while (ad.inWaiting()==0):
            pass
        dataPacket=ad.readline().rstrip()
        dataPacket=str(dataPacket,'utf-8')
        splitPacket=dataPacket.split(",")
        yaw=radians(float(splitPacket[6]))
        pitch=radians(float(splitPacket[7]))
        roll=radians(float(splitPacket[8]))
        print(splitPacket[0], splitPacket[1], splitPacket[2])

        #rate(50)
        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll)+cross(k,v)*sin(roll)
        k1 = -k
        side1 = -cross(k,vrot)
        up1 = vrot

        frontArrow.axis=k1
        sideArrow.axis=side1
        upArrow.axis=up1

        myObj.axis=k1
        myObj.up=up1
        sideArrow.length=2
        frontArrow.length=4
        upArrow.length=1


    except:
        pass
