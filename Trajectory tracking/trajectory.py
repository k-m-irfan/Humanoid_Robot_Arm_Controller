from vpython import *
import math
import numpy as np
import serial
import time
serialData = serial.Serial('com7', 115200) #connecting to serial
scene.forward=vector(-1,-1,-1)

#testarrow1=arrow(length=4,shaftwidth=.1,color=color.green,axis=vector(0,0,1))
#testarrow2=arrow(length=4,shaftwidth=.1,color=color.yellow,axis=vector(0,0,1))
#testarrow3=arrow(length=4,shaftwidth=.1,color=color.red,axis=vector(0,0,1))

#t1=arrow(length=4,shaftwidth=.1,color=color.green,axis=vector(0,0,1))
#t2=arrow(length=4,shaftwidth=.1,color=color.yellow,axis=vector(0,0,1))
#t3=arrow(length=4,shaftwidth=.1,color=color.red,axis=vector(0,0,1))

#ua=arrow(length=4,shaftwidth=.1,color=color.red,axis=vector(0,0,1))
#fa=arrow(length=4,shaftwidth=.1,color=color.green,axis=vector(0,0,1))
#pa=arrow(length=4,shaftwidth=.1,color=color.blue,axis=vector(0,0,1))
#pos=arrow(length=4,shaftwidth=.1,color=color.magenta,axis=vector(0,0,1))
ball = sphere(make_trail=True,radius=0.005,trail_radius=0.1)

Po = vector(0,0,0)
file = open("angles.txt","w")
ti = time.time()

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
            pitchIndex = radians(float(Data[11]))
            yawIndex = radians(float(Data[12]))
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
        
        # Index finger orientation###############
        k=vector(cos(yawIndex)*cos(pitchIndex), sin(pitchIndex),sin(yawIndex)*cos(pitchIndex))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll2)+cross(k,v)*sin(roll2)
        k3 = -k
        side3 = -cross(k,vrot)
        up3 = vrot

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

       # testarrow1.axis = k3
        #testarrow1.length = 4
        #testarrow2.axis = side3
        #testarrow2.length = 4
        #testarrow3.axis = up3
        #testarrow3.length = 4

        #t1.axis = vector(float(Data[19]), float(Data[20]), float(Data[21]))
        #t1.length = 2
        #t2.axis = vector(float(Data[22]), float(Data[23]), float(Data[24]))
        #t2.length = 2
        #t3.axis = vector(float(Data[25]), float(Data[26]), float(Data[27]))
        #t3.length = 2
        
       # print(int(ang_shr)," , ",int(ang_shh)," , ", int(ang_bcprot)," , ",int(ang_elbow)," , ", int(ang_wristrot)," , ", int(ang_wristx)," , ", int(ang_wristy))
        #print(ang_bcprot , ":", Data[21])
        
        #Hand Position---------------------------------------------------
        #ua.axis = 2*k0
        #fa.axis = 2*k1
        #pa.axis = 2*k2
        P = 10*(k0+k1+0.4*k2+0.4*k3)
        Pn = 0.85*Po+0.15*P
        ball.pos = Pn
        tt = time.time()-ti
        #print("X:","%.2f" % Pn.x,"Y:", "%.2f" % Pn.y,"Z:", "%.2f" % Pn.z)
        #file.write(str(Pn.x)+", "+str(Pn.y)+", "+str(Pn.z)+"\n")
        file.write(str(tt)+" , "+str(ang_shr)+", "+str(ang_shh)+", "+str(ang_bcprot)+", "+str(ang_elbow)+", "+str(ang_wristrot)+", "+str(ang_wristx)+", "+str(ang_wristy)+" , " +str(pitchIndex)+" , " +str(yawIndex)+" , " + str(Pn.x)+", "+str(Pn.y)+", "+str(Pn.z)+"\n")
        Po = Pn
file.close()
        
