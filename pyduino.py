import serial
import time

locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3','/dev/ttyACM4','/dev/ttyACM5','/dev/ttyACM6','/dev/ttyACM7','/dev/ttyACM8',  
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']    
    
for device in locations:    
    try:    
        print "Trying...",device  
        ser = serial.Serial(device, 9600)   
        break  
    except:    
        print "Failed to connect on",device     
  
counter = 0
outputLibrary = ['A', 'B', 'C']

while True:
	value = ser.read()
	if value == 'L':
		if counter > 1 and counter < 5:
			print('hit: '+ outputLibrary[int(value)]+" " + str(counter))
			counter = 0
		elif counter > 5:
			print('Lo')
			counter = 0
		else:		
			print('Lo')
	elif value is not 'L':
		counter += 1
		if counter < 5 and counter > 1:
			print('hit: '+ outputLibrary[int(value)] +" " + str(counter) )
		elif counter > 6:
			print('hold: '+ outputLibrary[int(value)]+" " + str(counter))
	
		
	