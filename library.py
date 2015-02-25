import re

class Library(object):
	"""docstring for Library"""
	def __init__(self, name):
		self.name = name
		#[Fingers; Serial Equivilent]
		self.index_array 	= [ 'P1', 'P2', 'R1', 'R2', 'M1', 'M2', 'I1', 'I2',
								'3', '1', '2', '4', '8', '5', '6', '7']
		self.string_array 	= [ 'P1', 'P2', 'R1', 'R2', 'M1', 'M2', 'I1', 'I2',
								'','','','','','','','']	
		self.library_array 	= [ 'P1', 'P2', 'R1', 'R2', 'M1', 'M2', 'I1', 'I2',
								'','','','','','','','']			
		self.file_array	 	= [ 'P1', 'P2', 'R1', 'R2', 'M1', 'M2', 'I1', 'I2',
								'','','','','','','','']			 


	def LoadFromFile(self, keyfile):
		f = open(keyfile,'r') 
		for line in f.readlines():
			self.AssignKeyByDelimitedLine(line)

	def LoadFromName(self):
		pass

	def LoadDefaultLibrary(self):
		self.LoadFromFile('Libraries/default')

	def LoadFromSet(self):
		pass

	def GetLibraryKeys(self):
		pass

	def GetLocalLibrarySet(self):
		pass

	#index:string:holdlibraryname:holdlibraryfile
	def AssignKeyByDelimitedLine(self,line):
		l = re.split(':',line)
		index = self.index_array.index(l[0])+8
		self.string_array[index] = l[1]
		self.library_array[index] = l[2]
		if l[3][len(l[3])-1] == '\n':
			self.file_array[index] = l[3][0:len(l[3])-1]
		else:
			self.file_array[index] = l[3][0:len(l[3])]
		print('success:' + l[1] +' assigned to:' + l[0])

	def CheckLibraryFlags(self):
		pass


		