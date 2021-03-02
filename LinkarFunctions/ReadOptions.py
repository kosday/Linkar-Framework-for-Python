from .CommonOptions import CommonOptions

"""
	Class: ReadOptions
		Object that works as an argument in Read function and defines the function options.
				
	Property: Calculated
		boolean
		
		Returns the resulting values from the calculated dictionaries.
	Property: Conversion
		boolean
		
		Executes the defined conversions in the dictionaries before returning.
	Property: FormatSpec
		string
		
		Executes the defined formats in the dictionaries before returning.
	Property: OriginalRecords
		boolean
		
		Returns a copy of the records in MV format.
"""
class ReadOptions:
	"""
		Constructor: constructor
			Initializes a new instance of the ReadOptions class
			
		Arguments:
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			conversion - (boolean) Execute the defined conversions in the dictionaries before returning.
			formatSpec - (boolean) Execute the defined formats in the dictionaries before returning.
			originalRecords - (boolean) Return a copy of the records in MV format.
		
	"""
	def __init__(self, calculated=False, conversion=False, formatSpec=False, originalRecords=False):
		self.CommonOptions = CommonOptions(calculated, conversion, formatSpec, originalRecords)
		self.Calculated = self.CommonOptions.Calculated
		self.Conversion = self.CommonOptions.Conversion
		self.FormatSpec = self.CommonOptions.FormatSpec
		self.OriginalRecords = self.CommonOptions.OriginalRecords


	"""
		Function: GetString
			Composes the Read options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
			
			The string ready to be used by LinkarSERVER
	"""
	def GetString(self):
		return self.CommonOptions.GetStringAM()