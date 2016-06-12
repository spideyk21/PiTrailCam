#!/usr/bin/env python3
#title           : pitrailcam_pir-test2.py
#description     : check PIR sensor input
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#notes           : http://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/
#
#python_version  : 3
#notes		 : uses gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, MotionSensor
from signal import pause
import time
import picamera

pir = MotionSensor(17) #set pir pin number
#led = LED(#) #set led pin number

camera = picamera.PiCamera()

while True:
	pir.wait_for_motion()
#	print("Motion detected!")
#	ts = time.strftime("%Y%m%d_%H%M%S")
#	camera.capture('/home/pi/Pictures/' + ts + '.jpg')
#	camera.close()

	with picamera.PiCamera() as camera:
		camera.capture('foo.jpg')

	time.sleep(5)
	

pause()

