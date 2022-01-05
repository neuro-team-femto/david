#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:28:00 2018

@author: liuni


pyDAVID v1.0

Usage examples with parameters' description and configuration
"""

import time

import pydavid


# for MIC input
sfrecname = ["example"] # filename of the output transformed soundfile

#for SOUNDFILE input
sfplayname = ["/Users/liuni/IRCAM_SYNC/CREAM/pydavid/1-neutral_exc.wav"] # filename (absolute path) of the input soundfile


# for ALL input
sfolderrecname = ["/Users/liuni/IRCAM_SYNC/CREAM/pydavid/"] # path of the folder for the output transformed soundfile


preset = 2 # number of preset to apply


pitchshift = 200 # pitch shift value (cents)

hold = 0 # time before the automation ramp starts (milliseconds)
ramp = 0 # duration of the automation ramp (milliseconds)

marker_name = ["/Users/liuni/IRCAM_SYNC/CREAM/pydavid/example.txt"] # filename (absolute path) for the text file of time markers


###############################################################################

# create OSC server
user = pydavid.pydavid('localhost')
user.connect()


# MicRecord - preset applied on the input audio and stored as a soundfile, 
# with a separate text file for markers 

user.MicRecord(sfrecname, preset, hold, ramp, sfolderrecname)
time.sleep(3)
user.StopMicRecord()

print 'ok'



## MicPitchShift - pitch shift applied on the input audio and stored as a soundfile, 
## with a separate text file for markers 
#
#user.MicPitchShift(sfrecname,100,1.5,0,'marker_1', sfolderrecname)
#time.sleep(3)
#user.StopMicRecord()
#time.sleep(1)
#user.StoreMarkers(marker_name)

#print 'ok'



## SfRecord - preset applied on the input soundfile; two output files are stored: 
## sfplayname
#
#
#user.SfRecord(sfplayname, preset, hold, ramp, sfolderrecname)
#time.sleep(5)
#
#print 'ok'



time.sleep(1)
user.disconnect()