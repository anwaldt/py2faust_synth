"""
@date Created on Sun Mar 10 11:49:02 2019

@author: anwaldt
"""

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from pythonosc import osc_message_builder as omb


import numpy

import time


class synth_osc_player():
    
    
    def __init__(self, pitch, cutoff, deltaT, OSCP):

        self.pitch   = pitch        
        self.cutoff  = cutoff
        self.L       =  pitch.__len__()        
        self.osc     = OSCP
        
        self.dT      = deltaT/1000
        
        # quick helpers for note triggering
        self.counter = 0        
        self.state   = 0
        
    def run_sequence(self):
                
        idx = numpy.arange(0,self.L)
        
        for i in idx:            
            
            
            tmp_pitch  = self.pitch[i]
            tmp_cutoff = self.cutoff[i]

 
                        
            outPath = "/subtractive_synth/fc"        
            msg     = omb.OscMessageBuilder(address=outPath)    
            msg.add_arg(tmp_cutoff)                            
            msg     = msg.build()       
            self.osc.send(msg)

    
            outPath = "/subtractive_synth/freq"        
            msg     = omb.OscMessageBuilder(address=outPath)    
            msg.add_arg(tmp_pitch)                            
            msg     = msg.build()       
            self.osc.send(msg)



            if self.counter%100 == 0:                
                      
                outPath = "/subtractive_synth/gater"        
                msg     = omb.OscMessageBuilder(address=outPath)    
                
                if self.state==0:
                    msg.add_arg(1)     
                    self.state=1
                    
                elif self.state==1:
                    msg.add_arg(0)          
                    self.state=0
                    
                msg     = msg.build()       
                self.osc.send(msg)       


            time.sleep(self.dT)         
            
            self.counter = self.counter+1
 
    

    