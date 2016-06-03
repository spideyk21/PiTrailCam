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
#				   http://richardhayler.blogspot.co.uk/2016/05/naturebytes-lite-bare-bones-build-for.html
#
#python_version  : 3.0 (sudo apt-get install python3-picamera)
#notes			 : written using gpiozero (https://gpiozero.readthedocs.org/)
#==============================================================================

# Import required Python libraries
from gpiozero import LED, MotionSensor, Button
import picamera
from signal import pause
from datetime import datetime
import time
import os
import logging

#Dip Switch Settings
dip_cmode = Button(#) #capture mode: picture/video (false=picture, true=video)
dip_pmode = Button(#) #Picture/Time-Lapse Mode (false=Single Picture, false=Time Lapse)
dip_time1 = Button(#) #Time #1 Delay Between Time Lapse Pictures, or Length of Video to Capture
dip_time2 = Button(#) #Time #2 Delay Between Time Lapse Pictures, or Length of Video to Capture
dip_time3 = Button(#) #Time #3 Delay Between Time Lapse Pictures, or Length of Video to Capture

camera = picamera.PiCamera
pir = MotionSensor(#) #set pir pin number
led = LED(#) #set led pin number

date = time.strftime("%Y%m%d_%H%M%S")
pic_loc = "/home/pi/trailcam/pictures/"
vid_loc = "/home/pi/trailcam/videos/"

def take_picture():
	#os.system ("raspistill -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
	camera.capture('image.jpg')

def take_video():
	#os.system ("raspivid -n -vf -hf -o " + pic_loc + DATE + ".jpg") #sh command
	camera.start_recording('video.h264')
	
while True:
    pir.wait_for_motion()
#    logging.info('Motion detected')
    print('Motion detected')
    while pir.motion_detected:
        print('Taking photo')
        ts  ='{:%H%M%S-%d%m%Y}'.format(datetime.now())
#        logging.info('Taking photo: '+ str(ts)+'.jpg')
        with picamera.PiCamera() as cam:
            cam.resolution=(1024,768)
            cam.capture('/home/pi/'+str(ts)+'.jpg')
        time.sleep(0.5)
    print('Motion Ended')

#    logging.info('Motion Ended')