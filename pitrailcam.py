#!/usr/bin/env python
#title           : pitrailcam.py
#description     : Raspberry Pi based Trailcam
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#refrence        : http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
#				   http://www.afraidofsunlight.co.uk/weather/trailcam_info.html
#
#python_version  : 3.0
#notes			 : written using gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, MotionSensor, Button
from signal import pause
import time
import os

#Dip Switch Settings
dip_cmode = Button(#) #capture mode: picture/video (false=picture, true=video)
dip_pmode = Button(#) #Picture/Time-Lapse Mode (false=Single Picture, false=Time Lapse)
dip_time1 = Button(#) #Time #1 Delay Between Time Lapse Pictures, or Length of Video to Capture
dip_time2 = Button(#) #Time #2 Delay Between Time Lapse Pictures, or Length of Video to Capture
dip_time3 = Button(#) #Time #3 Delay Between Time Lapse Pictures, or Length of Video to Capture

pir = MotionSensor(#) #set pir pin number
led = LED(#) #set led pin number

date = time.strftime("%Y%m%d_%H%M%S")
pic_loc = "/home/pi/trailcam/pictures/"
vid_loc = "/home/pi/trailcam/videos/"

def take_picture():
	os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command

def take_video():
	os.system ("raspivid -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
	
	
while True:
	pir.wait_for_motion()
	print("Motion detected!")

pause()