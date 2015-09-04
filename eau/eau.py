#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

nbTop = 0

def cb(arg):
    global nbTop
    nbTop = nbTop + 1
    print "impulsion !"


GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.add_event_detect(23,GPIO.FALLING)
GPIO.add_event_callback(23,cb)

while True:
    nbTop = 0
    time.sleep(1)
    Calc = (nbTop * 60 / 7.5)
    print "Calc: %d L/hour" % Calc
