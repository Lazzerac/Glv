import serial
import string
import math
import struct

from time import time

grad2rad = 3.141592/180.0

# Check your COM port and baud rate
# ser = serial.Serial(port='COM7',baudrate=115200, timeout=1)
locations=['/dev/ttyUSB0','/dev/ttyUSB1']

for device in locations:    
    try:    
        print "Trying...",device  
        ser = serial.Serial(device ,baudrate=115200, timeout=1)
        break  
    except:    
        print "Failed to connect on",device     

f = open("Serial"+str(time())+".txt", 'w')
i = 0 

while 1:
    s_line = ser.read()
    if struct.unpack('<c',s_line)[0] == '!':
        s_line2 = ser.read(size=8)
        s2 = struct.unpack('hhhh',s_line2)
        if s2[3] != 8:
            print s2
ser.close
f.close
