from vpython import *
import math
import numpy as np
import serial
serialData = serial.Serial('com4', 115200) #connecting to serial

scene.background = color.white

#Making Base,Post and Shoulder Base
#base = box(pos=vector(0,0,0), length=3, height=.3, width=3, color=vector(0,0,1))
#post = curve(pos=[vector(0,0,0), vector(0,6,0), vector(1.5,6,0)], radius=0.3,color=vector(0,1,0))
shoulderBase = cylinder(pos=vector(1.5,6,0),radius=.4,axis=vector(1,0,0),length=.3,color=vector(1,0,0))

#Making Shoulder Joint
shoulderRevolve = cylinder(pos=vector(1.8,6,0),radius=.4,axis=vector(1,0,0),length=.3,color=vector(1,1,0))
ShoulderHinge1 = box(pos=vector(2.3,6,-.18), length=.5, height=.4, width=.1, color=vector(1,1,0))
ShoulderHinge2 = box(pos=vector(2.3,6,.18), length=.5, height=.4, width=.1, color=vector(1,1,0))
shoulderPart = compound([shoulderRevolve,ShoulderHinge1,ShoulderHinge2],axis=vector(1,0,0))
#Shoulder reference axis
rod1 = cylinder(pos=vector(2.4,6,0),radius=.02,axis=vector(0,0,1),length=1,color=vector(1,0,0),opacity=0)

#Making Bicep
bcp1 = box(pos=vector(2.4,6,0),length=.4,height=.4,width=.25,color=vector(1,1,1))
bcp2 = cylinder(pos=vector(2.6,6,0),radius=.2,axis=vector(1,0,0),length=0.5,color=vector(1,1,1))
bcp3 = cylinder(pos=vector(3.1,6,0),radius=.25,axis=vector(1,0,0),length=.1,color=vector(1,1,1))
bcep1 = compound([bcp1,bcp2,bcp3],axis=vector(1,0,0))

bcp4 = cylinder(pos=vector(3.2,6,0),radius=.25,axis=vector(1,0,0),length=.1,color=vector(0,1,1))
bcp5 = cylinder(pos=vector(3.3,6,0),radius=.2,axis=vector(1,0,0),length=0.5,color=vector(0,1,1))
bcp6 = box(pos=vector(4,6,0),length=.4,height=.4,width=.25,color=vector(0,1,1))
bcep2 = compound([bcp4,bcp5,bcp6],axis=vector(1,0,0))
#elbow reference axis
rod2 = cylinder(pos=vector(4,6,0),radius=.02,axis=vector(0,0,1),length=1,color=vector(1,0,0),opacity=0)
#elbow reference object
elbow_ref = box(pos=vector(4,6,0),length=.4,height=.4,width=.25,color=vector(1,1,0.5),opacity=0)
elbow_ref.rotate(angle=radians(90),axis=vector(0,1,0))

#making arm
armHinge1 = box(pos=vector(4.05,6,-.18), length=.5, height=.4, width=.1, color=vector(1,0,1))
armHinge2 = box(pos=vector(4.05,6,.18), length=.5, height=.4, width=.1, color=vector(1,0,1))
armHinge3 = box(pos=vector(4.3,6,0), length=.1, height=.4, width=.45, color=vector(1,0,1))
armPart1 = cylinder(pos=vector(4.35,6,0),radius=.2,axis=vector(1,0,0),length=0.7,color=vector(1,0,1))
armPart2 = cylinder(pos=vector(5.05,6,0),radius=.25,axis=vector(1,0,0),length=.1,color=vector(1,0,1))
arm1 = compound([armHinge1,armHinge2,armHinge3,armPart1,armPart2])

armPart3 = cylinder(pos=vector(5.15,6,0),radius=.25,axis=vector(1,0,0),length=.1,color=vector(0.5,0.5,0.5))
armPart4 = cylinder(pos=vector(5.25,6,0),radius=.2,axis=vector(1,0,0),length=0.5,color=vector(0.5,0.5,0.5))
arm2 = compound([armPart3,armPart4])

#making palm
palmShape = [ [0,0], [-0.1,0.7], [0.6,0.7], [0.5,0], [0,0] ]#Shape of palm
palmPath = [vector(0,0,0),vector(0,0,0.2)]#extrusion path
palm = extrusion(path=palmPath, shape=palmShape, color=color.red, pos=vector(6.225,6,0), axis=vector(0,-1,0))
palm.size = 0.85*palm.size#adjusting size of palm

#wrist reference object
wrist_ref1 = box(pos=vector(5.85,6,0),length=.25,height=.25,width=.25,color=vector(0.5,0.5,1))
wrist_ref1.rotate(angle=radians(90),axis=vector(0,1,0))
wrist_ref2 = box(pos=vector(5.95,6,0),length=.25,height=.25,width=.25,color=vector(0.5,0.5,1))
wrist_ref2.rotate(angle=radians(-90),axis=vector(0,0,1))
#wrist reference axis
rod3 = cylinder(pos=wrist_ref1.pos,radius=.02,axis=vector(0,0,1),length=1,color=vector(1,0,0),opacity=0)
rod4 = cylinder(pos=wrist_ref2.pos,radius=.02,axis=vector(0,1,0),length=1,color=vector(1,0,0),opacity=0)

#making fingers
f01 = box(pos=vector(6.22,6.25,-0.13),length=0.25,height=0.1,width=0.13,color=color.blue)
f01.rotate(angle=radians(25),axis=vector(0,0,1))
f02 = box(pos=vector(6.445,6.25,-0.13),length=0.2,height=0.1,width=0.13,color=color.red)
f02.rotate(angle=radians(25),axis=vector(0,0,1),origin=f01.pos)
f03 = box(pos=vector(6.62,6.25,-0.13),length=0.15,height=0.1,width=0.13,color=color.yellow)
f03.rotate(angle=radians(25),axis=vector(0,0,1),origin=f01.pos)

f11 = box(pos=vector(6.64,6.24,0),length=0.95*0.25,height=0.13,width=0.1,color=color.blue)
f12 = box(pos=vector(6.85,6.24,0),length=0.95*0.2,height=0.13,width=0.1,color=color.red)
f13 = box(pos=vector(7.015,6.24,0),length=0.95*0.15,height=0.13,width=0.1,color=color.yellow)

f21 = box(pos=vector(6.645,6.08,0),length=0.25,height=0.13,width=0.1,color=color.blue)
f22 = box(pos=vector(6.87,6.08,0),length=0.2,height=0.13,width=0.1,color=color.red)
f23 = box(pos=vector(7.045,6.08,0),length=0.15,height=0.13,width=0.1,color=color.yellow)

f31 = box(pos=vector(6.64,5.92,0),length=0.95*0.25,height=0.13,width=0.1,color=color.blue)
f32 = box(pos=vector(6.85,5.92,0),length=0.95*0.2,height=0.13,width=0.1,color=color.red)
f33 = box(pos=vector(7.015,5.92,0),length=0.95*0.15,height=0.13,width=0.1,color=color.yellow)

f41 = box(pos=vector(6.62,5.76,0),length=0.8*0.25,height=0.13,width=0.1,color=color.blue)
f42 = box(pos=vector(6.8,5.76,0),length=0.8*0.2,height=0.13,width=0.1,color=color.red)
f43 = box(pos=vector(6.94,5.76,0),length=0.8*0.15,height=0.13,width=0.1,color=color.yellow)

#finger reference objects
f0a1 = box(pos=vector(6.1,6.195,-0.13),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f0a1.rotate(angle=radians(25),axis=vector(0,0,1))
f0a2 = box(pos=vector(6.1,6.195,-0.13),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f0a2.rotate(angle=radians(25),axis=vector(0,0,1))
f0a3 = box(pos=vector(6.35,6.195,-0.13),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f0a3.rotate(angle=radians(25),axis=vector(0,0,1),origin=f0a2.pos)
f0a4 = box(pos=vector(6.55,6.195,-0.13),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f0a4.rotate(angle=radians(25),axis=vector(0,0,1),origin=f0a2.pos)

f1a1 = box(pos=vector(6.52,6.24,0),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f1a2 = box(pos=vector(6.52,6.24,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f1a3 = box(pos=vector(6.7575,6.24,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f1a4 = box(pos=vector(6.9475,6.24,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)

f2a1 = box(pos=vector(6.52,6.08,0),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f2a2 = box(pos=vector(6.52,6.08,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f2a3 = box(pos=vector(6.77,6.08,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f2a4 = box(pos=vector(6.97,6.08,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)

f3a1 = box(pos=vector(6.52,5.92,0),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f3a2 = box(pos=vector(6.52,5.92,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f3a3 = box(pos=vector(6.7575,5.92,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f3a4 = box(pos=vector(6.9475,5.92,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)

f4a1 = box(pos=vector(6.52,5.76,0),length=0.08,width=0.08,height=0.08,axis=vector(0,0,-1),color=vector(0,1,0),opacity=0)
f4a2 = box(pos=vector(6.52,5.76,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f4a3 = box(pos=vector(6.72,5.76,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)
f4a4 = box(pos=vector(6.88,5.76,0),length=0.08,width=0.08,height=0.08,axis=vector(0,1,0),color=vector(0,1,0),opacity=0)

#testarrow1=arrow(length=4,shaftwidth=.1,color=color.green,axis=vector(0,0,1))
#testarrow2=arrow(length=4,shaftwidth=.1,color=color.yellow,axis=vector(0,0,1))
#testarrow3=arrow(length=4,shaftwidth=.1,color=color.red,axis=vector(0,0,1))

#defining initial joint angles as 0 degrees
preang_a = 0
preang_b = 0
preang_c = 0
preang_d = 0
preang_e = 0
preang_f = 0
preang_g = 0
preang_f0x = 0
preang_f0y = 0
preang_f1x = 0
preang_f1y = 0
preang_f2x = 0
preang_f2y = 0
preang_f3x = 0
preang_f3y = 0
preang_f4x = 0
preang_f4y = 0

while True:
#############################################################################################
    if (serialData.inWaiting()>0): #Start reading data if it is available
        Data = serialData.readline().rstrip()
        try:
            Data = Data.decode().split(",")
        except:
            continue
        if len(Data) != 19:
            continue

        try:
            yaw0 = radians(float(Data[0])+90)
            pitch0 = radians(float(Data[1]))
            roll0 = radians(float(Data[2]))
            yaw1 = radians(float(Data[3])+90)
            pitch1 = radians(float(Data[4]))
            roll1 = radians(float(Data[5]))
            yaw2 = radians(float(Data[6])+90)
            pitch2 = radians(float(Data[7]))
            roll2 = radians(float(Data[8]))
            ang_f0y = float(Data[9])+60
            ang_f0x = float(Data[10])+10
            ang_f1y = float(Data[11])
            ang_f1x = float(Data[12])
            ang_f2y = float(Data[13])
            ang_f2x = float(Data[14])+10
            ang_f3y = float(Data[15])
            ang_f3x = float(Data[16])
            ang_f4y = float(Data[17])*2
            ang_f4x = float(Data[18])
        except:
            continue

        # IMU0 orientation (reference)
        k=vector(cos(yaw0)*cos(pitch0), sin(pitch0),sin(yaw0)*cos(pitch0))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll0)+cross(k,v)*sin(roll0)
        k0 = cross(k,vrot)
        side0 = -k
        up0 = vrot

        # IMU1 orientation (wrist)
        k=vector(cos(yaw1)*cos(pitch1), sin(pitch1),sin(yaw1)*cos(pitch1))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll1)+cross(k,v)*sin(roll1)
        k1 = -k
        side1 = -cross(k,vrot)
        up1 = vrot

        # IMU2 orientation (palm)
        k=vector(cos(yaw2)*cos(pitch2), sin(pitch2),sin(yaw2)*cos(pitch2))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll2)+cross(k,v)*sin(roll2)
        k2 = -k
        side2 = -cross(k,vrot)
        up2 = vrot

        ang_wristy = 90-degrees(diff_angle(k2,up1))
        ang_wristx = 90-degrees(diff_angle(k2,side1))
        ang_wristrot = -(90-degrees(diff_angle(side1,up0)))
        ang_elbow = degrees(diff_angle(k0,k1))

        k0_yz = vector(0,k0.y,k0.z)#k0component in yz plane
        bcp_ref1 = cross(k0_yz,vector(1,0,0))
        #if (k0.z>0):
         #   bcp_ref1 = -bcp_ref1
        bcp_ref2 = cross(k0,k1)

        ang_bcprot = -degrees(diff_angle(bcp_ref1,bcp_ref2))+90
        ang_shr = -degrees(math.atan2(k0.y,k0.z))-90
        ang_shh = degrees(math.atan2(k0.x,sqrt(k0.y*k0.y+k0.z*k0.z)))

        #testarrow1.axis = k1
        #testarrow1.length = 4
        #testarrow2.axis = side1
        #testarrow2.length = 4
        #testarrow3.axis = up1
        #testarrow3.length = 4
        
        print(float(ang_shr), float(ang_shh), float(ang_bcprot), float(ang_elbow), float(ang_wristrot), float(ang_wristx), float(ang_wristy))

#############################################################################################
    #taking input joint angles

        a = ang_shr#input("shoulder rotation angle (0 --> 360): ")#shoulder rotation angle
        a = float(a)
        ang_a = a-preang_a#changes are made with reference to its new position
        preang_a = a

        b = ang_shh #input("shoulder hinge angle (0 --> 180): ")#shoulder hinge angle
        b = float(b)-90
        ang_b = b-preang_b
        preang_b = b

        c = ang_bcprot#input("bicep rotation angle (-90 --> 90): ")#bicep rotation angle on its axis
        c = float(c)-90
        ang_c = c-preang_c
        preang_c = c

        d = ang_elbow#input("elbow hinge angle (0 -->180): ")#elbow hinge angle
        d = -float(d)
        ang_d = d-preang_d
        preang_d = d

        e = ang_wristrot#input("forearm rotation angle (-90 --> 90): ")#arm rotation angle
        e = float(e)
        ang_e = e-preang_e
        preang_e = e

        f = ang_wristx#input("wrist rotational angle (about rod3 axis)(-90 --> 90): ")#palm angle about rod3 axis
        f = float(f)
        ang_f = f-preang_f
        preang_f = f

        g = ang_wristy#input("wrist rotational angle (about rod4 axis)(-90 --> 90): ")#palm angle about rod4 axis
        g = float(g)
        ang_g = g-preang_g
        preang_g = g

        f0x = ang_f0x#input("thumb angle (about rod3 axis)(-30 --> 30): ")#thumb angle about rod3 axis
        f0x = float(f0x)
        ang_f0x = f0x-preang_f0x
        preang_f0x = f0x

        f0y = ang_f0y#input("thumb angle (about rod4 axis)(-30 --> 30): ")#thumb angle about rod4 axis
        f0y = float(f0y)
        ang_f0y = f0y-preang_f0y
        preang_f0y = f0y

        f1x = ang_f1x#input("index angle (about rod3 axis)(-30 --> 30): ")#index angle about rod3 axis
        f1x = float(f1x)
        ang_f1x = f1x-preang_f1x
        preang_f1x = f1x

        f1y = ang_f1y#input("index angle (about rod4 axis)(-30 --> 30): ")#index angle about rod3 axis
        f1y = float(f1y)
        ang_f1y = f1y-preang_f1y
        preang_f1y = f1y

        f2x = ang_f2x#input("middle angle (about rod3 axis)(-30 --> 30): ")#middle angle about rod3 axis
        f2x = float(f2x)
        ang_f2x = f2x-preang_f2x
        preang_f2x = f2x

        f2y = ang_f2y#input("middle angle (about rod4 axis)(-30 --> 30): ")#middle angle about rod3 axis
        f2y = float(f2y)
        ang_f2y = f2y-preang_f2y
        preang_f2y = f2y

        f3x = ang_f3x#input("ring angle (about rod3 axis)(-30 --> 30): ")#ring angle about rod3 axis
        f3x = float(f3x)
        ang_f3x = f3x-preang_f3x
        preang_f3x = f3x

        f3y = ang_f3y#input("ring angle (about rod4 axis)(-30 --> 30): ")#ring angle about rod3 axis
        f3y = float(f3y)
        ang_f3y = f3y-preang_f3y
        preang_f3y = f3y

        f4x = ang_f4x#input("pinky angle (about rod3 axis)(-30 --> 30): ")#pinky angle about rod3 axis
        f4x = float(f4x)
        ang_f4x = f4x-preang_f4x
        preang_f4x = f4x

        f4y = ang_f4y#input("pinky angle (about rod4 axis)(-30 --> 30): ")#pinky angle about rod3 axis
        f4y = float(f4y)
        ang_f4y = f4y-preang_f4y
        preang_f4y = f4y

    else:#loop continues
        continue

#rotating shoulder part wrt ang_a
    shoulderPart.rotate(angle=radians(ang_a))
    rod1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))#rotating axis wrt to ang_a

#rotating bcep1 wrt ang_b (child to shoulderPart)
    bcep1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    bcep1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)

#rotating bcep2 wrt ang_c (child to bcep1)
    bcep2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    bcep2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    bcep2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)

#to get reference elbow position and axis
    elbow_ref.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    elbow_ref.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    elbow_ref.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    rod2.pos = elbow_ref.pos
    rod2.axis = elbow_ref.axis
    rod2.length = 1

#rotating arm1 wrt ang_c and ang_d(child to bcep2)
    arm1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    arm1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    arm1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    arm1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)

#rotating arm2 wrt ang_e(child to arm1)
    arm2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    arm2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    arm2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    arm2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    arm2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)

#to get reference wrist position and axes linked with the arm2
    wrist_ref1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    wrist_ref1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    wrist_ref1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    wrist_ref1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    wrist_ref1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)

    wrist_ref2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    wrist_ref2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    wrist_ref2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    wrist_ref2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    wrist_ref2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)

    rod3.pos = wrist_ref1.pos
    rod3.axis = wrist_ref1.axis
    rod3.length = 1

    wrist_ref2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)

    rod4.pos = wrist_ref2.pos
    rod4.axis = wrist_ref2.axis
    rod4.length = 1

#rotating palm wrt ang_f and ang_g (child to arm2)
    palm.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    palm.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    palm.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    palm.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    palm.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    palm.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    palm.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

#linking of fingers (child to palm)
#thumb--------------------------------------------------------------------------
    f01.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f01.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f01.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f01.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f01.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f01.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f01.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f02.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f02.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f02.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f02.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f02.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f02.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f02.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f03.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f03.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f03.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f03.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f03.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f03.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f03.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#index--------------------------------------------------------------------------
    f11.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f11.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f11.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f11.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f11.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f11.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f11.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f12.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f12.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f12.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f12.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f12.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f12.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f12.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f13.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f13.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f13.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f13.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f13.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f13.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f13.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#middle-------------------------------------------------------------------------
    f21.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f21.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f21.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f21.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f21.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f21.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f21.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f22.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f22.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f22.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f22.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f22.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f22.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f22.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f23.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f23.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f23.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f23.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f23.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f23.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f23.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#ring---------------------------------------------------------------------------
    f31.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f31.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f31.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f31.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f31.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f31.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f31.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f32.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f32.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f32.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f32.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f32.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f32.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f32.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f33.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f33.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f33.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f33.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f33.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f33.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f33.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#pinky--------------------------------------------------------------------------
    f41.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f41.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f41.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f41.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f41.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f41.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f41.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f42.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f42.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f42.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f42.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f42.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f42.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f42.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f43.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f43.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f43.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f43.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f43.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f43.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f43.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

#linking finger reference cubes with palm as parent
#thumb--------------------------------------------------------------------------
    f0a1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f0a1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f0a1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f0a1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f0a1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f0a1.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f0a1.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f0a2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f0a2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f0a2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f0a2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f0a2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f0a2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f0a2.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f0a3.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f0a3.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f0a3.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f0a3.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f0a3.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f0a3.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f0a3.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f0a4.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f0a4.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f0a4.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f0a4.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f0a4.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f0a4.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f0a4.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#index--------------------------------------------------------------------------
    f1a1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f1a1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f1a1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f1a1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f1a1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f1a1.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f1a1.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f1a2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f1a2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f1a2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f1a2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f1a2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f1a2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f1a2.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f1a3.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f1a3.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f1a3.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f1a3.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f1a3.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f1a3.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f1a3.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f1a4.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f1a4.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f1a4.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f1a4.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f1a4.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f1a4.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f1a4.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#middle-------------------------------------------------------------------------
    f2a1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f2a1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f2a1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f2a1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f2a1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f2a1.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f2a1.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f2a2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f2a2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f2a2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f2a2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f2a2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f2a2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f2a2.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f2a3.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f2a3.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f2a3.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f2a3.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f2a3.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f2a3.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f2a3.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f2a4.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f2a4.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f2a4.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f2a4.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f2a4.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f2a4.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f2a4.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#ring---------------------------------------------------------------------------
    f3a1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f3a1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f3a1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f3a1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f3a1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f3a1.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f3a1.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f3a2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f3a2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f3a2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f3a2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f3a2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f3a2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f3a2.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f3a3.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f3a3.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f3a3.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f3a3.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f3a3.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f3a3.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f3a3.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f3a4.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f3a4.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f3a4.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f3a4.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f3a4.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f3a4.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f3a4.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)
#pinky--------------------------------------------------------------------------
    f4a1.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f4a1.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f4a1.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f4a1.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f4a1.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f4a1.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f4a1.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f4a2.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f4a2.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f4a2.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f4a2.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f4a2.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f4a2.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f4a2.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f4a3.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f4a3.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f4a3.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f4a3.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f4a3.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f4a3.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f4a3.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

    f4a4.rotate(angle=radians(ang_a),axis=vector(1,0,0),origin=vector(2.4,6,0))
    f4a4.rotate(angle=radians(ang_b),axis=rod1.axis,origin=rod1.pos)
    f4a4.rotate(angle=radians(ang_c),axis=bcep1.axis,origin=bcep1.pos)
    f4a4.rotate(angle=radians(ang_d),axis=rod2.axis,origin=rod2.pos)
    f4a4.rotate(angle=radians(ang_e),axis=arm1.axis,origin=arm1.pos)
    f4a4.rotate(angle=radians(ang_f),axis=rod3.axis,origin=rod3.pos)
    f4a4.rotate(angle=radians(ang_g),axis=rod4.axis,origin=rod4.pos)

#finger movement
#thumb--------------------------------------------------------------------------
    f01.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)
    f0a2.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)#ref box
    f0a3.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)#ref box
    f0a4.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)#ref box
    f02.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)
    f03.rotate(angle=radians(ang_f0x),origin=f0a1.pos,axis=f0a1.axis)

    f01.rotate(angle=radians(ang_f0y),origin=f0a2.pos,axis=f0a2.axis)
    f02.rotate(angle=radians(ang_f0y),origin=f0a2.pos,axis=f0a2.axis)
    f03.rotate(angle=radians(ang_f0y),origin=f0a2.pos,axis=f0a2.axis)
    f0a3.rotate(angle=radians(ang_f0y),origin=f0a2.pos,axis=f0a2.axis)#ref box
    f0a4.rotate(angle=radians(ang_f0y),origin=f0a2.pos,axis=f0a2.axis)#ref box
#index--------------------------------------------------------------------------
    f11.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)
    f1a2.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)#ref box
    f1a3.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)#ref box
    f1a4.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)#ref box
    f12.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)
    f13.rotate(angle=radians(ang_f1x),origin=f1a1.pos,axis=f1a1.axis)

    f11.rotate(angle=radians(ang_f1y),origin=f1a2.pos,axis=f1a2.axis)
    f12.rotate(angle=radians(ang_f1y),origin=f1a2.pos,axis=f1a2.axis)
    f13.rotate(angle=radians(ang_f1y),origin=f1a2.pos,axis=f1a2.axis)
    f1a3.rotate(angle=radians(ang_f1y),origin=f1a2.pos,axis=f1a2.axis)#ref box
    f1a4.rotate(angle=radians(ang_f1y),origin=f1a2.pos,axis=f1a2.axis)#ref box
#middle-------------------------------------------------------------------------
    f21.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)
    f2a2.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)#ref box
    f2a3.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)#ref box
    f2a4.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)#ref box
    f22.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)
    f23.rotate(angle=radians(ang_f2x),origin=f2a1.pos,axis=f2a1.axis)

    f21.rotate(angle=radians(ang_f2y),origin=f2a2.pos,axis=f2a2.axis)
    f22.rotate(angle=radians(ang_f2y),origin=f2a2.pos,axis=f2a2.axis)
    f23.rotate(angle=radians(ang_f2y),origin=f2a2.pos,axis=f2a2.axis)
    f2a3.rotate(angle=radians(ang_f2y),origin=f2a2.pos,axis=f2a2.axis)#ref box
    f2a4.rotate(angle=radians(ang_f2y),origin=f2a2.pos,axis=f2a2.axis)#ref box
#ring---------------------------------------------------------------------------
    f31.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)
    f3a2.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)#ref box
    f3a3.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)#ref box
    f3a4.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)#ref box
    f32.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)
    f33.rotate(angle=radians(ang_f3x),origin=f3a1.pos,axis=f3a1.axis)

    f31.rotate(angle=radians(ang_f3y),origin=f3a2.pos,axis=f3a2.axis)
    f32.rotate(angle=radians(ang_f3y),origin=f3a2.pos,axis=f3a2.axis)
    f33.rotate(angle=radians(ang_f3y),origin=f3a2.pos,axis=f3a2.axis)
    f3a3.rotate(angle=radians(ang_f3y),origin=f3a2.pos,axis=f3a2.axis)#ref box
    f3a4.rotate(angle=radians(ang_f3y),origin=f3a2.pos,axis=f3a2.axis)#ref box
#pinky--------------------------------------------------------------------------
    f41.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)
    f4a2.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)#ref box
    f4a3.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)#ref box
    f4a4.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)#ref box
    f42.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)
    f43.rotate(angle=radians(ang_f4x),origin=f4a1.pos,axis=f4a1.axis)

    f41.rotate(angle=radians(ang_f4y),origin=f4a2.pos,axis=f4a2.axis)
    f42.rotate(angle=radians(ang_f4y),origin=f4a2.pos,axis=f4a2.axis)
    f43.rotate(angle=radians(ang_f4y),origin=f4a2.pos,axis=f4a2.axis)
    f4a3.rotate(angle=radians(ang_f4y),origin=f4a2.pos,axis=f4a2.axis)
    f4a4.rotate(angle=radians(ang_f4y),origin=f4a2.pos,axis=f4a2.axis)

#finger segment movements
#thumb--------------------------------------------------------------------------
    f02.rotate(angle=radians(ang_f0x),origin=f0a3.pos,axis=f0a3.axis)
    f0a4.rotate(angle=radians(ang_f0x),origin=f0a3.pos,axis=f0a3.axis)
    f03.rotate(angle=radians(ang_f0x),origin=f0a3.pos,axis=f0a3.axis)
    f03.rotate(angle=radians(ang_f0x),origin=f0a4.pos,axis=f0a4.axis)
#index--------------------------------------------------------------------------
    f12.rotate(angle=radians(ang_f1y),origin=f1a3.pos,axis=f1a3.axis)
    f1a4.rotate(angle=radians(ang_f1y),origin=f1a3.pos,axis=f1a3.axis)
    f13.rotate(angle=radians(ang_f1y),origin=f1a3.pos,axis=f1a3.axis)
    f13.rotate(angle=radians(ang_f1y),origin=f1a4.pos,axis=f1a4.axis)
#middle-------------------------------------------------------------------------
    f22.rotate(angle=radians(ang_f2y),origin=f2a3.pos,axis=f2a3.axis)
    f2a4.rotate(angle=radians(ang_f2y),origin=f2a3.pos,axis=f2a3.axis)
    f23.rotate(angle=radians(ang_f2y),origin=f2a3.pos,axis=f2a3.axis)
    f23.rotate(angle=radians(ang_f2y),origin=f2a4.pos,axis=f2a4.axis)
#ring---------------------------------------------------------------------------
    f32.rotate(angle=radians(ang_f3y),origin=f3a3.pos,axis=f3a3.axis)
    f3a4.rotate(angle=radians(ang_f3y),origin=f3a3.pos,axis=f3a3.axis)
    f33.rotate(angle=radians(ang_f3y),origin=f3a3.pos,axis=f3a3.axis)
    f33.rotate(angle=radians(ang_f3y),origin=f3a4.pos,axis=f3a4.axis)
#pinky--------------------------------------------------------------------------
    f42.rotate(angle=radians(ang_f4y),origin=f4a3.pos,axis=f4a3.axis)
    f4a4.rotate(angle=radians(ang_f4y),origin=f4a3.pos,axis=f4a3.axis)
    f43.rotate(angle=radians(ang_f4y),origin=f4a3.pos,axis=f4a3.axis)
    f43.rotate(angle=radians(ang_f4y),origin=f4a4.pos,axis=f4a4.axis)
