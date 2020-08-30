#!/usr/bin/env python3

###############################################################################
"""Script for creating control trajectories for measuring the GLOOO system."""
# 
#
"""Author: HvC"""
"""Date: 2020-08-30"""
#
###############################################################################

import subprocess
import os
import numpy
 


from pythonosc import dispatcher
from pythonosc import udp_client
from pythonosc import osc_message_builder as omb

import synth_osc_player as sop



glooo_OSC = udp_client.SimpleUDPClient("127.0.0.1", 5510)

deltaT    = 10;  # control timing in ms
L         = 10;  # stimulus length in s

nPoints   = round(L/(deltaT/1000));

t  = numpy.linspace(0,L,nPoints)


###############################################################################
""" Method for starting a complete recording process."""
###############################################################################

def param_sweep(fStart, fStop, iStart, iStop, ifilename):
    
    pro = subprocess.Popen(['jack_capture --channels 1 -d ' +str(L) + ' -p subtractive_synth:out_0 '+filename], 
                       stdout=subprocess.PIPE, 
                       shell=True, 
                       preexec_fn=os.setsid) 
 
    
    # arrays with parameter trajectories
    pitch  = numpy.linspace(iStart,iStop,num=nPoints)
    cutoff = numpy.linspace(fStart,fStop,num=nPoints)
    
    p1 = sop.synth_osc_player(pitch,cutoff,deltaT,glooo_OSC)
    
    p1.run_sequence()
 
 

t = numpy.linspace(0,5,num=nPoints)

###############################################################################

###############################################################################

# Pitch sweep 1
filename = "../wav/test_1.wav"
param_sweep(0, 5000, 50, 50, filename)

 
 
 