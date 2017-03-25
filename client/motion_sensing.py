from SF_9DOF import IMU
import time
import os
import sys
import math
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("131.179.9.11", 1200))
gyroAngleX = 0
gyroAngleY = 0
gyroAngleZ = 0
hasSteped = 0
steps = 0
G_GAIN = .07
Gth = 2.5
Ath = .2
AZth = .015
# Create IMU object
imu = IMU() # To select a specific I2C port, use IMU(n). Default is 1. 

# Initialize IMU
imu.initialize()

# Enable accel, mag, gyro, and temperature
imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()
imu.enable_temp()

# Set range on accel, mag, and gyro

# Specify Options: "2G", "4G", "6G", "8G", "16G"
imu.accel_range("2G")       # leave blank for default of "2G" 

# Specify Options: "2GAUSS", "4GAUSS", "8GAUSS", "12GAUSS"
imu.mag_range("2GAUSS")     # leave blank for default of "2GAUSS"

# Specify Options: "245DPS", "500DPS", "2000DPS" 
imu.gyro_range("245DPS")    # leave blank for default of "245DPS"

#create files
afile = "ACCEL.txt"
ad = open(afile, 'w')
gfile = "GYRO.txt"
gd = open(gfile, 'w')
mfile = "MAG.txt"
md = open(mfile, 'w')
tfile = "TIME.txt"
td = open(tfile, 'w')

start_time = time.time()
aZ0 = 0
stepTime = 0 
endStepTime = 0
tick = 0
totalTime = 0
timeStamp = 0
count = 0
startGyro = 0
tX = 0
tY = 0
# Loop and read accel, mag, and gyro
while(1):
#gather imu data    
    imu.read_accel()
    imu.read_mag()
    imu.read_gyro()
    imu.readTemp()

    #timeE = time.time() - start_time
    
        #convert Gyro raw to dps
    gyroX = imu.gx * G_GAIN
    gyroY = imu.gy * G_GAIN
    gyroZ = imu.gz * G_GAIN
    
    #filter gyro noise
    if gyroZ > -1 and gyroZ < 1:
        gyroZ = 0
    if gyroY > -1 and gyroY < 1:
        gyroY = 0
    if gyroX > -1 and gyroX < 1:
        gyroX = 0
        
    #calculate angles from gyro
    gyroAngleX +=gyroX*.1
    gyroAngleY +=gyroY*.1
    if gyroZ == 0:
        gyroAngleZ = 0
    gyroAngleZ +=gyroZ*.1
    
    turn = 0
    if startGyro == 0:
        if gyroAngleZ > Gth:
          #  print "gyroAngleZ" + str(gyroAngleZ) + "Right"
            turn = 1
            startGyro = 1
        if gyroAngleZ < -Gth:
          #  print "gyroAngleZ" + str(gyroAngleZ) + "Left"
            turn = -1
            startGyro = 1
    if gyroAngleZ == 0 and startGyro == 1: 
        startGyro = 0
#cancel gravity
    aZ = imu.az+1
   # print "Accel: " + str(aZ)
#get starting accel
    if count == 0:
        aZ0 = aZ
        dX = 0
        dY = 0

#write test data files
   # ad.write("%.8f\t %.8f\t %.8f\n" % (imu.ax, imu.ay, imu.az))
   # gd.write("%.8f\t %.8f\t %.8f\n" % (gyroX, gyroY, gyroZ))
   # md.write("%.8f\t %.8f\t %.8f\n" % (imu.mx, imu.my, imu.mz))

#initial values for step counting
    stepCount = 0

#if we take a step (threshold = -.2)
    if aZ < -Ath  and hasSteped == 0:
        print "AccelZ: " + str(aZ) + " aZ0: " + str(aZ0)
        stepCount = 1
        hasSteped = 1
       # stepTime = time.time()- start_time
        #tick = 0

#if we stop (threshold is +- .015 original accel)
    if aZ < (AZth+aZ0) and aZ > (-AZth+aZ0):
        hasSteped = 0
        #tick += 1
        #if tick == 1:
         #    endStepTime = time.time() - start_time

   # if tick== 1:
     #   totalTime +=endStepTime-stepTime
        
   # steps = 0
    if stepCount:
        steps+=1
        print "Turn: " + str(turn) + " Step: " + str(steps)

    if turn != 0 or count%20==0:
        print "Turn: " + str(turn) + " Step: " + str(steps)
         
        
        #send the data a an array data = [, dY, timeStamp]
        data = "" + str(turn) + "\t" + str(steps) 
        print 'send to server: ' + data
        client_socket.send(data)
        while client_socket.recv(2048) != "ack":
            print "waiting for server"
        print "awk received!"
        steps = 0
        

    count+=1
    #td.write("%s\n"% (timeE))
 #Sleep for 1/10th of a second
    time.sleep(0.1)


dmsg = "disconnect"
print "Disconnecting"
client_socket.send(dmsg)

client_socket.close()
