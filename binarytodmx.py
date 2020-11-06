# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:48:48 2020

@author: kelli
"""

import numpy as np
import random

class binaryToDMX:
    
    def __init__(self, values, tStart, tEnd, tStep):
        
        #function used to get channel values
        self.values = values
        
        #define total time and number of frames
        self.tStart = tStart
        self.tStep = tStep
        self.time = tEnd - tStart
        self.nFrames = int(self.time/tStep)    

        
    def write(self):
        """ Create binary frames and write to file
        """
        file = open('binaryDMX.bin', 'wb')

        for i in range(self.nFrames):
            b = bytearray(512)
            frame = (self.values(self.tStart+i*self.tStep))
            for j in range(512):
                b[j:j+1]=bytes(frame[j])
                
            #okay I think this is just over writing it each time.... how do I fix this 
            file.write(b)
                
        file.close()   

#this is a test function, returns a random int up to 256 for 512 channels
def testValues(t):
    values = np.zeros(512)
    for i in range(512):
        values[i] = random.randint(0, 256)
    return values
            
if __name__ == '__main__':
    
    # start time  = 0s, end time = 10s, increment .5s   
    test = binaryToDMX(testValues, 0, 10, .5)
    test.write()    
        
        