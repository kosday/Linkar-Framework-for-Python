from . import DBMV_Mark
from .CommonOptions import CommonOptions

"""
	Class: ReadAfterCommonOptions
		Auxiliary class with the ReadAfters options for <UpdateOptions> and <NewOptions> classes.
		
		*Extends:* <CommonOptions>
		
	Property: ReadAfter
		boolean
		
		Reads the record again and returns it after the update or new. <CommonOptions.Calculated>, <CommonOptions.Conversion>, <CommonOptions.FormatSpec> and <CommonOptions.OriginalRecords> properties will only make effect if this option is true.
"""
class ReadAfterCommonOptions(CommonOptions):
	"""
		Constructor: constructor
		
		Arguments:
			readAfter - (boolean) Reads the record again and returns it after the update or new. Calculated, conversion, formatSpec and originalRecords will only make effect if this option is true.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			conversion - (boolean) Execute the defined conversions in the dictionaries before returning.
			formatSpec - (boolean) Execute the defined formats in the dictionaries before returning.
			originalRecords - (boolean) Return a copy of the records in MV format.
	"""
	def __init__(self, readAfter=False, calculated=False, conversion=False, formatSpec=False, originalRecords=False):
		super().__init__(calculated, conversion, formatSpec, originalRecords)
		self.ReadAfter = readAfter


	"""
		Function: GetStringAM
			Composes the ReadAfterCommonOptions options string for use with <UpdateOptions> and <NewOptions> classes.
			
		Returns:
			string
			
			The string ready to be used by <UpdateOptions> and <NewOptions> classes
	"""
	def GetStringAM(self):
		return "1" if self.ReadAfter else "0" + DBMV_Mark.AM_str + super().GetStringAM()