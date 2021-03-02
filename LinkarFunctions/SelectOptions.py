from . import DBMV_Mark
from .CommonOptions import CommonOptions

"""
	Class: SelectOptions
		Object that works as an argument in Select function and defines the function options.
		
	Property: OnlyRecordId
		boolean
		
		Returns just the selected records codes.
	
	Property: Pagination
		boolean
		
		Indicates if pagination is being used or not.
		
	Property: Pagination_RegPage
		number
		
		In case of pagination indicates the number of records by page. It must be bigger than 0.
		
	Property: Pagination_NumPage
		number
		
		In case of pagination it indicates the page number to obtain. Must be greater than 0.
		
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

class SelectOptions:
	"""
		Constructor: __init__()
			Initializes a new instance of the SelectOptions class.
			
		Arguments:
			onlyRecordId - (boolean) Returns just the ID(s) of selected record(s).
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			conversion - (boolean) Execute the defined conversions in the dictionaries before returning.
			formatSpec - (boolean) Execute the defined formats in the dictionaries before returning.
			originalRecords - (boolean) Return a copy of the records in MV format.
	"""
	def __init__(self, onlyRecordId = False, pagination = False, regPage = 10, numPage = 0, calculated = False, conversion = False, formatSpec = False, originalRecords = False):
		self.CommonOptions =  CommonOptions(calculated, conversion, formatSpec, originalRecords)
		self.OnlyRecordId = onlyRecordId;
		self.Pagination = pagination;
		self.Pagination_RegPage = regPage;
		self.Pagination_NumPage = numPage;
		self.Calculated = self.CommonOptions.Calculated;
		self.Conversion = self.CommonOptions.Conversion;
		self.FormatSpec = self.CommonOptions.FormatSpec;
		self.OriginalRecords = self.CommonOptions.OriginalRecords;


	"""
		Function: GetString
			Composes the Select options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
			
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		return "1" if self.Pagination else "0" + DBMV_Mark.VM_str + self.Pagination_RegPage + DBMV_Mark.VM_str + self.Pagination_NumPage + DBMV_Mark.AM_str + "1" if self.OnlyRecordId else "0" + DBMV_Mark.AM + self.CommonOptions.GetStringAM()