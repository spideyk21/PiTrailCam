#!/usr/bin/env python
#title           : pitrailcam2.py
#description     : Raspberry Pi based Trailcam
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#refrence        : http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   http://picamera.readthedocs.io/
#				   https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
#				   http://www.afraidofsunlight.co.uk/weather/trailcam_info.html
#				   http://richardhayler.blogspot.co.uk/2016/05/naturebytes-lite-bare-bones-build-for.html
#
#python_version  : 3.0 (sudo apt-get install python3-picamera)
#notes			 : written using gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import MotionSensor, Button, LED
from picamera import PiCamera
import time

pir = MotionSensor(17)
camera = PiCamera()

dip_cmode = Button(#) #capture mode: picture/video (true=picture, false=video)
dip_pmode = Button(#) #Picture Mode: Motion Activated=true, Time Lapse=false

#dip_time1 = Button(#)
#dip_time2 = Button(#)
#dip_time3 = Button(#)

#extra
#dip_button6 = Button(#)
#dip_button7 = Button(#)
#dip_button8 = Button(#)

pic_loc: "/home/pi/Pictures/"
vid_loc: "home/pi/Videos/"


while True:
	pir.wait_for_motion()
	print("Motion Detected")
	filename = time.strftime("%Y%m%d_%H%M%S")
	camera.resolution = (1024,768)
	camera.capture('/home/pi/Pictures/' + filename + '.jpg')
	time.sleep(2)
