#!/usr/bin/python

import math, time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

ADC_COUNTS = 1<<12
ICAL = 1

def readAmp(nbSamples):
    SupplyVoltage = 2700

    sumI = 0
    offsetI = 0
    for n in range(0, nbSamples):
        sampleI = adc.readADCSingleEnded(1, gain, sps)

        # Digital low pass filter extracts the 2.5 V or 1.65 V dc offset,
        # then subtract this - signal is now centered on 0 counts.
        # useless offsetI = (offsetI + (sampleI-offsetI)/1024)
        offsetI = 2509
        filteredI = sampleI - offsetI

        # Root-mean-square method current
        # 1) square current values
        sqI = filteredI * filteredI
        # 2) sum
        sumI += sqI

    # useless I_RATIO = ICAL *((SupplyVoltage/1000.0) / (ADC_COUNTS))
    Irms = (math.sqrt(sumI / nbSamples) / 300) * 2000 - 22

    return Irms

gain = 4096
sps = 3200
adc = ADS1x15(ic=0) # 12 bits
while True:
    #debug amp = adc.readADCSingleEnded(1, gain, sps)
    amp = readAmp(200)
    print "%.6f W" % (amp)
    time.sleep(0.5)
