from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions
from .LkData import LkData

"""
	Class: LkDataSubroutine
		Class to management the result of the operations Subroutine.
		
		Property: Arguments
		string array
		
		Argument list of the Subroutine operation execution.
"""
class LkDataSubroutine(LkData):

	"""
		Constructor: __init__
			Initializes a new instance of the LkDataCRUD class.
			
		Arguments:
			subroutineResult - (string) The string result of the Subroutine operation execution.
	"""
	def __init__(self, subroutineResult):
		super().__init__(subroutineResult)
		self.Arguments = StringFunctions.ExtractSubroutineArgs(subroutineResult)
