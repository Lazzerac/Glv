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
	
	def LoadLibraryByFingerByName(self, index):
	 	ser_index = self.index_array.index(index)
	 	finger_index = ser_index-8
	 	finger = self.key_array[finger_index]

		pass

	def LoadLibraryByFingerByFile(self, index):
	 	ser_index = self.index_array.index(index)
	 	finger_index = ser_index-8
	 	finger = self.key_array[finger_index]
	 	lib_index = self.library_array.index(finger)+8
	 	self.lib = library.Library(library_array[lib_index])
	 	self.lib.LoadLibraryByFile(self.file_array[lib_index])
	 	self.index_array = self.lib.index_array
		self.library_array = self.lib.library_array
		self.file_array = self.lib.file_array
		
		pass

	# def LoadLibraryByName(self,library_name):
	# 	pass

	# def LoadLibraryByFile(self,library_file_location):
	# 	pass

	def ResetLibrary(self):
		pass