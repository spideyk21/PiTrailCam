#!/usr/bin/env python
#title           : pitrailcam_pir-test.py
#description     : check PIR sensor input
#author          : spideyk21
#date            : MM/DD/YYYY
#version         : X.X
#usage           : 
#notes           : http://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/
#
#python_version  : 2.7
#==============================================================================

# Import required Python libraries
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 17

print "PIR Module Test (CTRL-C to exit)"

# Set GPIO pins (input/output)
GPIO.setup(GPIO_PIR,GPIO.IN) #pir

Current_State  = 0
Previous_State = 0

try:
  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Ready"     
    
  # Loop until users quits with CTRL-C
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      # PIR is triggered
	  print ("Motion detected!)
	  
	  # Record previous state
	  Previous_State=1
	  
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
      
    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
