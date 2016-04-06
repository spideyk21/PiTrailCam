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
#python_version  : 2.7
#==============================================================================

# Import required Python libraries
import RPi.GPIO as GPIO

#pic_loc = "/home/pi/webcam/"
pic_loc = "/media/LinHES_201502/"
DATE = time.strftime("%Y%m%d_%H%M%S")

print pic_loc

# Take Picture with options
os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh
