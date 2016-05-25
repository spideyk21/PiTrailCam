#!/usr/bin/env python
#title           : pitrailcam_pir-test2.py
#description     : check PIR sensor input
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#notes           : http://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, MotionSensor
from signal import pause

pir = MotionSensor(17) #set pir pin number
led = LED(#) #set led pin number

while True:
	pir.wait_for_motion()
	print("Motion detected!")

pause()
