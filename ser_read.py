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
hold = False
while True:
	text = ser.read(size=3)
	#print(text)
	if text > 0:
	 	value = int(float(text))
	else:
	 	value = 0
	#print(value)
	
	# if last_read_byte > 1 and last_read_byte < 10 and value == 1:
	# 	last_read_byte = 1
	# 	pass
	# if value == last_read_byte + 10:
	# 	print('LRB1: ' + str(last_read_byte)+" V: "+ str(value))
	# 	last_read_byte = value
	# 	pass
	# if value < 10 and last_read_byte > 10:
	# 	print('LRB2: '+ str(last_read_byte) +" V: "+ str(value))
	# 	last_read_byte = value
	# 	pass
	
	if last_read_byte > 10 and value < 10 and hold == True:
		print('LRB3: '+ str(last_read_byte)+" V: "+ str(value))
		pass

	#Output single tap
	elif value < 10 and value > 0 and hold == False:
		print('LRB4: '+ str(last_read_byte) +" V: "+ str(value))
		#print(glove.index_array)
		ser_index = glove.index_array.index(str(value))
		#print(ser_index)
		finger_index = ser_index-8
	 	finger = glove.key_array[finger_index]
	 	output = output_array[output_array.index(finger)+8]
	 	print(output)
	 	last_read_byte = value
	
	#Holding; last:hold current: hold 	
	elif value > 10 and value == last_read_byte:
		print('LRB5: '+ str(last_read_byte) +" V: "+ str(value))
		finger = glove.GetFingerBySerialIndex(str(value))
	 	glove.LoadLibraryByFingerByFile(finger)
	 	output_array = glove.key_array
	 	index = value;
	 	last_read_byte = value;
	 	hold = True
	 	#glove.loadLibrary(LibrarySet[index])
	 	#print('2')
	 	pass

	elif value > 10 and last_read_byte < 10 :
		last_read_byte = value
		print('LRB6: '+ str(last_read_byte)+" V: "+ str(value))
		hold = True
		pass
	
