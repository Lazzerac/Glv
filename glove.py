import library 

class Glove:
	"""docstring for Glove  """
	def __init__(self, name):
		self.name = name
		self.lib = library.Library('00')
		self.lib.LoadDefaultLibrary()
		self.key_array = self.lib.string_array
		self.index_array = self.lib.index_array
		self.library_array = self.lib.library_array
		self.file_array = self.lib.file_array

	def SetKeyArray(self):
		pass
	
	def LoadLibraryArrays(self):
		self.key_array = self.lib.string_array
		self.index_array = self.lib.index_array
		self.library_array = self.lib.library_array
		self.file_array = self.lib.file_array
		pass
	
	def GetFingerBySerialIndex(self, index):
	 	ser_index = self.index_array.index(str(int(index)-10))
	 	finger_index = ser_index-8
	 	finger = self.key_array[finger_index]
		return finger

	def LoadLibraryByFinger(self, index):
		f = self.GetFingerBySerialIndex(index)
		self.lib.LoadLibraryByFile()
		
	def LoadLibraryByFingerByFile(self, finger):
	 	lib_index = self.library_array.index(finger)+8
	 	if self.library_array[lib_index] == '0':
	 		pass
	 	elif self.lib.name == self.library_array[lib_index]:
	 		pass
	 	else:
	 		self.lib = library.Library(self.library_array[lib_index])
	 		self.lib.LoadFromFile(self.file_array[lib_index])
			self.LoadLibraryArrays()

		pass

	# def LoadLibraryByName(self,library_name):
	# 	pass

	# def LoadLibraryByFile(self,library_file_location):
	# 	pass

	def ResetLibrary(self):
		pass