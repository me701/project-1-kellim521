"""
Read and write .rc2 files given DMX.

  1. Header
  2. Sequence of Show Control Frames

Header is 512 bytes.
  - 00000h to 00007h: ASCII string SHC21.00
    Note:
     bytes('SHC21.00', 'ascii').hex()
    gives
     '53484332312e3030'
  - 001FBh to 001FFh: number of frames
    (1FBh and 1FFh from 7FB and 7FF, typo)
    4 byte (unsigned 16 bit); little endian.
    A little-endian system stores the least-significant byte at the
    smallest address.
  - unused bytes set to 00h

Frames are 545 bytes and begin at 00200h.
  - 00000h to 001FFh: Value of the 512 channels of the DMX512 output (512 bytes)
    set at 00h by default.
  - 00200h: Value of the 8x output contacts (1 bytes).
    Bit 1 = state of the output contact 1
    Bit 2 = state of the output contact 2, ...
    Bit 8 = state of the output contact 8.
    0 = output contact opened, 1 = output contact closed.
  - 00201h to 00220h: Unused data, can be set to 00h

"""


import codecs
import math
import numpy as np


class RC2:
    
    header_size = 512
    frame_size = 545
    
    
    def __init__(self, filename, numFrames):
        self.filename = filename
        
    def write(self, binaryData):
        """ Write the data. Goal is to recreate identical .sc2 file from one provided, so that
            any binary data can be converted to .sc2
        """
        
        # Write header
        b = bytearray(799482)
        b[0:8] = b'SHC21.00'
        b[(self.header_size-4):self.header_size] = numFrames.to_bytes(2, byteorder='little')
        
        #Write frames
        #for i in range(numFrames):
            
        
        f = open('newsc2.sc2', 'wb')
        return b
    
    def read(self):
        """ Read the data.
        """


        f = open(self.filename, 'rb')
        b = f.read()
        f.close()
        
        # Number of frames
        num_frames = int.from_bytes(b[(self.header_size-4):self.header_size], byteorder='little')

        print("there are {} frames".format(num_frames))

        frames = []
        for i in range(num_frames):
            
            start = i*self.frame_size + self.header_size
            stop = start + self.frame_size
            
            frame = b[start:stop]
            fr = []
            for j in range(len(frame)):
                fr.append(int.from_bytes(frame[j:j+1], byteorder='little'))
            frames.append(fr)
    
        self.frames = np.array(frames)
        return self.frames
        

        
        
if __name__ == '__main__':
    
    R = RC2('volcano.sc2')
    binaryFrames = R.read()
    
    newSC2 = R.write(binaryFrames, 1466) #change 1466 to something from read
