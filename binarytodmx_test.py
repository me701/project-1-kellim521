# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:03:22 2020

@author: kelli
"""

from binarytodmx import *
import unittest
import filecmp
    
class TestDMX(unittest.TestCase):
    
    def test_volcano(self):
        """ test with frame data in np array from volcano.sc2
            uses rc2 tools to read 'volcano.sc2' and store in array
        """
        
        volcano = rc2.RC2('volcano.sc2')
        volcanoFrames = volcano.read()
        volcanoTest = DMX(volcanoFrames, 0, 1466, 1)
        volcanoTest.write('VolcanoTest.bin')

        self.assertTrue(filecmp.cmp('VolcanoTest.bin', 'volcano.sc2'))
        
    def test_userinput(self):
        """tests user input and function supplying random 
            data, seeded from t
        """
        
        # start time  = 0s, end time = 10s, increment .5s   
        test = DMX(testValues, 0, 10, .5)
        test.write('RandomChannels.bin')
        
        file = userInput()
        self.assertTrue(filecmp.cmp(file, 'RandomChannels.bin'))
        
    
if __name__ == '__main__':

    unittest.main()