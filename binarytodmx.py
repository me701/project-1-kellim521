# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:48:48 2020

@author: kelli
"""

import numpy as np
import random
import rc2_tools as rc2

class DMX:
    
    def __init__(self, values, tStart, tEnd, tStep):
        """ creates DMX object
            ----------
            Parameters
            ----------
            values : function or array to use as channel data source
            tStart : start time for functino
            tEnd : end time for function
            tStep : time interval at which frames are captured
        """
        
        #function used to get channel values
        self.values = values
        
        #define total time and number of frames
        time = tEnd - tStart
        self.tStart = tStart
        self.tStep = tStep
        self.nFrames = int(time/tStep)
        
    def write(self, fileName):
        """ Create binary frames and write to file
        """
        file = open(fileName, 'wb')
        
        #write header
        bHeader = bytearray(512)
        bHeader[0:8] = b'SHC21.00'
        bHeader[508:512]=self.nFrames.to_bytes(4, byteorder='little')
        file.write(bHeader)
        
        # I am being lazy because I can't figure out how I can get my type
        # comparison to work
        compare = np.zeros(10)
        
        #write frames
        for i in range(self.nFrames):
            
            #check if values are in an array        
            if type(self.values) == type(compare):
                frame = self.values[i]
            
            else:
                # retrieves frame data using given function,
                frame = (self.values(self.tStart+i*self.tStep))
            
            # byte array to hold current frame
            bFrame = bytearray(545)
            
            # convert the frame data to binary and write each byte
            for j in range(len(frame)):
                bFrame[j:j+1] = int(frame[j]).to_bytes(1, byteorder='little')
            
            #write finished frame to file
            file.write(bFrame)
            
        file.close()

def testValues(t):
    """ test function, returns a random int up to 255 for 512 channels
    """
    random.seed(t)
    values = np.zeros(513)
    for i in range(513):
        values[i] = random.randint(0, 255)
    return values

def userInput():
    """ user inputs chaneel source function or array, start/end times, time
        step, and location to save binary output file
    """
    
    channelSource = input('function or array for channel data: ')
    tStart = eval(input('start time: '))
    tEnd = eval(input('end time: '))
    tStep = eval(input('time interval for each frame: '))
    file = input('save binary as: ')
    
    channels = DMX(eval(channelSource), tStart, tEnd, tStep)
    channels.write(file)    
    return file
            
if __name__ == '__main__':  

    userInput()
               