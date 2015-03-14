import serial
import string
import math

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

roll=0
pitch=0
yaw=0
while 1:
    line = ser.readline()
    #print line
    if line == '' or line == '\n' or line == '\r' or line == '\n\r' or line == '\r\n':
    	pass
    else:
	    f.write(line)                   # Write to the output log 
	    if line.find("!M:") != -1:
	    	print line[3]
ser.close
f.close
