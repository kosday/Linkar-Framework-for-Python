from LinkarStrings import StringFunctions
from .LkData import LkData


"""
	Class: LkDataFormat
		Class to management the result of the operations Format.
	
		Property: Format
		string
		
		The value of Format operation.
"""
class LkDataFormat(LkData):

	"""
		Constructor: __init__()
			Initializes a new instance of the LkDataCRUD class.
			
		Arguments:
			formatResult - (string) The string result of the Format operation execution.
	"""
	def __init__(self, formatResult):
		super().__init__(formatResult)
		self.Format = StringFunctions.ExtractFormat(formatResult)