from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions
from .LkData import LkData

"""
	Class: LkDataConversion
		Class to management the result of the operations Conversion.
		
		Property: Conversion
		string
		
		The value of the Conversion operation
"""
class LkDataConversion(LkData):

	"""
		Constructor: __init__
		
		Arguments:
			conversionResult - (string) The string result of the Conversion operation execution.
	"""
	def __init__(self, conversionResult):
		super().__init__(conversionResult)
		self.Conversion = StringFunctions.ExtractConversion(conversionResult)
		