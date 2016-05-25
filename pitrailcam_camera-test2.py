#!/usr/bin/env python
#title           : pitrailcam_camera-test.py
#description     : 
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#notes           : http://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md
#				   http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   http://www.afraidofsunlight.co.uk/weather/trailcam_info.html
#				   http://www.raspberrypi.org/documentation/usage/camera/python/README.md
#				   http://www.raspberrypi.org/documentation/usage/webcams/
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, MotionSensor
from signal import pause
import time
import os

button = Button(x) #set led pin number

pic_loc = "/home/pi/webcam/"
DATE = time.strftime("%Y%m%d_%H%M%S")

# Take Picture with options
def take_pic():
	os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
	time.sleep(1)

print (pic_loc)
button.when_pressed = take_pic

pause()