# ME 701 - Project 1 Report
#### DMX Data in Standard Binary Format<br />Kelli Ward

## DMX-512
DMX is a standardized method typically used for controlling lighting effects, and can also be found in special effects applications such as fog machines.
It operates over 512 potential channels. Each channel is one byte, so can represent contain 0-255. These channels are typically used to communicate RGB color.

The goal of my project is to take the information for those 512 channels for a set of time intervals or frames, and store it in a standard binary format that can be used by a DMX device to produce a light show. 

This project is a good one to tackle for ME701 in a few different ways. It definitely expanded my knowledge about binary data. I hadn't ever done anything in depth with binary file formats before. Additionally, I found the hardware aspect of this very interesting as well. The projects I always feel I learn the most in are the ones that have a tangible/real world application, because it forces you to work with something with very specific constraints. Finally, being one part of a larger group project also got me thinking about this project differently. Since I am not the one generating the DMX data from a music source, I had to test my code more thoroughly to make sure it would be able to handle an input that I didn't have access to for testing.

## Solution and Methods
My project is split into three files, `binarytodmx.py`, `binarytodmx_test.py`, and `rc2_tools.py`

 `binarytodmx.py` 
This is the main file in my project. When ran it takes user input for a channel data source, start time, end time, and frame interval, and saves the frames as a binary file also specified by the user. Additionally, the DMX class and write method it contains can be imported and used by other files as well. A DMX object is initialized with channel data source, start time, end time, and frame interval. The DMX object's write() method is makes up the bulk of the functionality of this project. This function writes the header data for the binary file, then converts each frame given through the function or array provided to the DMX object, then writes this frame to a binary file.
 
`binarytodmx_test.py`
I developed two different unit tests for my code, and would like to add a couple more for project two with different sources for data. The first compares a binary file in the .sc2 format used by commercial DMX devices to a file produced by my code for the same frame data. The second test uses a function with generates random frame data for time (t), and verifies that when the user enters a this function name and parameters, the two files produced match.

`rc2_tools.py`
Finally, I used a slightly modified version of this file provided on Canvas to read frame data from the volcano.sc2 file and store it in an array. This array is what I used as a data source for my first unit test.

## Results
## Repository
[Project 1](https://github.com/me701/project-1-kellim521)
