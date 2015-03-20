#import keyloader
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
  
#kl = keyloader.Keyloader()

while True:
	text = ser.read()
	print(text)
	if text == '\r' or text == '\n':
		pass
	elif text == '\x80' or text == '\x00':
		print(text)
		pass
	else:
		#print(text)
		#kl.options[text](text)
		pass
