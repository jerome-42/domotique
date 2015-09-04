#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

def cb(arg):
    print "impulsion !"


GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.add_event_detect(23,GPIO.FALLING)
GPIO.add_event_callback(23,cb)

while True:
    time.sleep(60)
