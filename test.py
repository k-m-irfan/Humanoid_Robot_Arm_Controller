from vpython import *
from time import *
import numpy as np
import math
import serial
scene.forward=vector(-1,-1,-1)

scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad

xarrow=arrow(lenght=2, shaftwidth=.1, color=color.red,axis=vector(1,0,0))
yarrow=arrow(lenght=2, shaftwidth=.1, color=color.green,axis=vector(0,1,0))
zarrow=arrow(lenght=2, shaftwidth=.1, color=color.blue,axis=vector(0,0,1))

frontArrow=arrow(length=4,shaftwidth=.1,color=color.purple,axis=vector(1,0,0))
upArrow=arrow(length=4,shaftwidth=.1,color=color.magenta,axis=vector(0,1,0))
sideArrow=arrow(length=4,shaftwidth=.1,color=color.orange,axis=vector(0,0,1))

while True:
    yaw = radians(float(input("yaw: ")))
    pitch = radians(float(input("pitch: ")))
    roll = radians(float(input("roll: ")))

    kz = vector(cos(yaw)*cos(pitch),-sin(pitch),sin(yaw)*cos(pitch))
    ky = vector(-sin(yaw)*cos(roll)+cos(yaw)*sin(pitch)*sin(roll), cos(pitch)*sin(roll), cos(yaw)*cos(roll)+sin(yaw)*sin(pitch)*sin(roll))
    kx = vector(sin(yaw)*sin(roll)+cos(yaw)*sin(pitch)*cos(roll), cos(pitch)*cos(roll), -cos(yaw)*sin(roll)+sin(yaw)*sin(pitch)*cos(roll))

    frontArrow.axis=kz
    frontArrow.length = 2
    sideArrow.axis=ky
    sideArrow.length = 2
    upArrow.axis=kx
    upArrow.length = 2
    print(kx, ky, kz)
