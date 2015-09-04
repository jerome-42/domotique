#!/usr/bin/python

import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

gain = 4096
sps = 250
adc = ADS1x15(ic=0) # 12 bits
while True:
    amp = adc.readADCSingleEnded(0, gain, sps) / 1000
    print "%.6f" % (amp)
    time.sleep(0.5)
