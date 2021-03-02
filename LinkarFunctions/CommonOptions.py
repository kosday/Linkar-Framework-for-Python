from . import DBMV_Mark

"""
	class: CommonOptions
		Auxiliary class with the common options for <ReadOptions>, <SelectOptions> and <ReadAfterCommonOptions> classes
		Property: Calculated 
			boolean
			
			Returns the resulting values from the calculated dictionaries.
		Property: Conversion
			boolean
			
			Executes the defined conversions in the dictionaries before returning.
		Property: FormatSpec
			boolean
			
			Executes the defined formats in the dictionaries before returning.
		Property: OriginalRecords
			boolean
			
			Returns a copy of the records in MV format.
"""

class CommonOptions:

	"""
		Constructor: constructor
			Initializes a new instance of the CommonOptions class.
		
		Arguments:
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			conversion - (boolean) Execute the defined conversions in the dictionaries before returning.
			formatSpec - (boolean) Execute the defined formats in the dictionaries before returning.
			originalRecords - (boolean) Return a copy of the records in MV format.
	"""

	def __init__(self, calculated=False, conversion=False, formatSpec=False, originalRecords=False):
		self.Calculated = calculated
		self.Conversion = conversion
		self.FormatSpec = formatSpec
		self.OriginalRecords = originalRecords

	"""
		Function: GetStringAM
			Composes the CommonOptions options string for use with <ReadOptions>, <SelectOptions> and <ReadAfterCommonOptions> classes.
			
		Return:
			string
			
			The string ready to be used by <ReadOptions>, <SelectOptions> and <ReadAfterCommonOptions> classes.
	"""
	def GetStringAM(self):
		return 	 + DBMV_MARK.AM_str + "" + DBMV_MARK.AM_str + "1" if self.Conversion else "0" + DBMV_MARK.AM_str + "1" if self.FormatSpec else "0" + DBMV_MARK.AM_str + "1" if self.OriginalRecords else "0"