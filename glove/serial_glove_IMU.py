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

#f = open("Serial"+str(time())+".txt", 'w')
i = 0 

while 1:
    s_line = ser.read()
    if struct.unpack('<c',s_line)[0] == '!':
        s_line2 = ser.read(size=8)
        s2 = struct.unpack('hhhH',s_line2)
        if s2[3] :
            print s2

    #s2 = struct.unpack_from('<chhhHc',s_line )
    #s1 = struct.unpack('<c',s_line[9])
    #print s2
        # pair1 = str(s_line[1] + s_line[2])
        # rec1 = struct.unpack('<h', pair1 )
        # pair2 = str(s_line[3] + s_line[4])
        # rec2 = struct.unpack('<h', pair2 )
        # pair3 = str(s_line[5] + s_line[6])
        # rec3 = struct.unpack('<h', pair3 )
        # pair4 = str(s_line[7] + s_line[8])
        # rec4 = struct.unpack('<H', pair4 )
        # # print rec1
        # # print rec2
        # # print rec3
        # # f.write("1:" + str(rec1[0]) + '\n')
        # # f.write("2:" + str(rec2[0])+ '\n')
        # # f.write("3:" + str(rec3[0])+ '\n')
        # f.write("4:" + str(rec4[0])+ '\n')
        # # print rec4
        # rec1 = ((rec1[0]/2**15)*math.pi - .5*math.pi)/grad2rad
        # rec2 = ((rec2[0]/2**15)*math.pi - .5*math.pi)/grad2rad
        # rec3 = ((rec3[0]/2**15)*math.pi - .5*math.pi)/grad2rad        


    # f.write(binascii.b2a_uu(s_line[0])[1]) 
    # f.write(binascii.b2a_uu(s_line[9])[1])
    # i =+ 1

    # try:
    #     if binascii.b2a_uu(s_line[9])[1] == "#" or binascii.b2a_uu(s_line[0])[1] == '"':
    #         rec1 = (s_line[1])*256 + s_line[2]
    #         rec2 = (s_line[3])*256 + s_line[4]
    #         rec3 = (s_line[5])*256 + s_line[6]
            
    #         rec1 = ((int(rec1)/2**15)*math.pi - .5*math.pi)/grad2rad
    #         rec2 = ((int(rec2)/2**15)*math.pi - .5*math.pi)/grad2rad
    #         rec3 = ((int(rec3)/2**15)*math.pi - .5*math.pi)/grad2rad
    #         f.write(str(rec1))
    #         i += 1
    #     else:
    #         pass
    # except:
    #     pass
    # s_line = binascii.b2a_uu(line[9])
    # f.write("0:"+ binascii.b2a_uu(line[0]))
    # f.write(line[1])
    # print line[1]
    # f.write(line[2])
    # print line[2]
    #f.write(line)
    # f.write("3:"+ line[3])
    # f.write("4:"+ line[4])
    # f.write("5:"+ line[5])
    # f.write("6:"+ line[6])
    # f.write("7:"+ line[7])
    # f.write("8:"+ line[8])
    # f.write("9:"+ binascii.b2a_uu(line[9]))            
    #print(line)
#     line = ser.read(size=10)
#     #line = ser.read()
#     try:
#         s_line = line.decode("utf-8")
#         f.write(s_line)
#         print(s_line)
#     except:
#         f.write(line)
#         pass
    # if str(line[0]) == '!'

    # print line
    # if line == '' or line == '\n' or line == '\r' or line == '\n\r' or line == '\r\n':
    # 	pass
    # else:
	   #  f.write(line)                   # Write to the output log 
	   #  if line.find("!M:") != -1:
	   #  	print line[3]

# while 1:
#     line = ser.readline()
#     print line
#     if line == '' or line == '\n' or line == '\r' or line == '\n\r' or line == '\r\n':
#     	pass
#     else:
# 	    f.write(line)                   # Write to the output log 
# 	    if line.find("!M:") != -1:
# 	    	print line[3]	    	
ser.close
f.close
