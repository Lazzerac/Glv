import glove

class Keyloader(object):
	"""docstring for Keyloader"""
	
	def key(self,key_index):
		self.loaded_key = key_index
		self.loaded_key_int = self.key_int(key_index)
		self.loaded_key_name = self.key_by_name(key_index)
		self.last_read_byte = 'K'
		
		pass	
	def on(self,key_index):
		self.on_increment =+ 1
		self.last_read_byte = 'O'
		pass

	def key_int(self, key_index):
		key = int(key_index)
		return key		

	def key_by_name(self, key_index):
		key = self.index_array.index(key_index)-8
		named_key = self.index_array[key]
		return named_key

	def release(self, key_index):
		if self.last_read_byte == 'H' and self.increment > 3:
			print(self.loaded_key_name)
			self.glove.LoadLibraryByFingerByFile(self.loaded_key_name)
			print(self.glove.lib.name)
			self.hold_flag = False
			self.increment = 0
			self.on_increment = 0

			self.last_read_byte = 'R'
			pass
		if self.last_read_byte == 'H' and self.increment == 1 or self.increment <= 3:
			output_index = self.glove.key_array.index(self.loaded_key_name)+8
			output = self.glove.key_array[output_index]
			print(output)
			self.hold_flag = False
			self.increment = 0
			self.on_increment = 0

			self.last_read_byte = 'R'
			pass
		elif self.last_read_byte == 'O' and self.on_increment > 0:
			output_index = self.glove.key_array.index(self.loaded_key_name)+8
			output = self.glove.key_array[output_index]
			print(output)
			self.hold_flag = False
			self.increment = 0
			self.on_increment = 0
			self.last_read_byte = 'R'
			pass
		elif self.last_read_byte == 'K':
			output_index = self.glove.key_array.index(self.loaded_key_name)+8
			output = self.glove.key_array[output_index]
			print(output)
			self.hold_flag = False
			self.increment = 0
			self.on_increment = 0
			self.last_read_byte = 'R'
			pass

	def hold(self,key_index):
		if self.increment > 3 and self.hold_flag == False:
			print("Holding.... \nNew Keyboard:")	
			self.hold_flag = True
		self.increment += 1
		self.last_read_byte = 'H'	
		pass 
	def passing(self,key_index):
		pass

	def __init__(self):
		self.options = {'1':self.key,
						'2':self.key,
						'3':self.key,
						'4':self.key,
						'5':self.key,
						'6':self.key,
						'7':self.key,
						'\x80':self.key,
						'R':self.release,
						'H':self.hold,
						'O':self.on}
		self.index_array = [ 'P1', 'P2', 'R1', 'R2', 'M1', 'M2', 'I1', 'I2',
								'3', '1', '2', '4', '8', '5', '8', '7']
		self.hold_flag = False
		self.glove = glove.Glove('11')
		self.on_increment = 0
		self.last_read_byte = '0'
		self.increment = 0



		# 	finger = glove.GetFingerBySerialIndex(str(value))
		#  	glove.LoadLibraryByFingerByFile(finger)
		#  	output_array = glove.key_array
			# pass

