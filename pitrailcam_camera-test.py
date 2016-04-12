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
import time
import os

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_BUTTON = 17

# Set GPIO pins (input/output)
GPIO.setup(GPIO_BUTTON,GPIO.IN, pull_up_down=GPIO.PUD_UP)


#pic_loc = "/home/pi/webcam/"
pic_loc = "/media/LinHES_201502/"
DATE = time.strftime("%Y%m%d_%H%M%S")

print pic_loc

try:  
 while True:
    if GPIO.input(switch_pin) == False:
        # Take Picture with options
		os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
		time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit