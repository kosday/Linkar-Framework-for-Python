from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions
"""
	Class: LkData
		Base class with common properties of all derived class.
	
	Property: OperationResult
	string
	
	The string that is obtained as result from the operation execution.
	
	Property: Errors
	string list
	
	List of the error of the operation execution.
	
"""
class LkData:

	"""
		Constructor: __init__
			Initializes a new instance of the LkData class.
		
		Arguments:
			opResult - (string) The string result of the operation execution.
	"""
	def __init__(self, opResult):
		self.OperationResult = opResult
		self.Errors = StringFunctions.ExtractErrors(opResult)
