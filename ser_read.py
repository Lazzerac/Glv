import glove
import serial
import time

#locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3','/dev/ttyACM4','/dev/ttyACM5','/dev/ttyACM6','/dev/ttyACM7','/dev/ttyACM8',  
#'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']    
locations=['/dev/ttyUSB0','/dev/ttyUSB1']

for device in locations:    
    try:    
        print "Trying...",device  
        ser = serial.Serial(device, 9600)   
        break  
    except:    
        print "Failed to connect on",device     
  
glove = glove.Glove('01')
last_read_byte = 0
output_array = glove.key_array
while True:
	text = ser.read(size=3)
	#print(text)
	if text > 0:
	 	value = int(float(text))
	else:
	 	value = 0

	if last_read_byte > 1 and last_read_byte < 10 and value == 1:
		last_read_byte = 1
		pass
	elif value > 10:
	 	finger = glove.GetFingerBySerialIndex(str(value))
	 	
	 	glove.LoadLibraryByFingerByFile(finger)
	 	output_array = glove.key_array
	 	index = value;
	 	last_read_byte = value;
	 	#glove.loadLibrary(LibrarySet[index])
	 	#print('2')
	elif value < 10:
		#print(glove.index_array)
		ser_index = glove.index_array.index(str(value))
		#print(ser_index)
		finger_index = ser_index-8
	 	finger = glove.key_array[finger_index]
	 	output = output_array[output_array.index(finger)+8]
	 	print(output)
	 	last_read_byte = value
	 	#print('3')
	else:
	 	#print('4')
		pass
		
