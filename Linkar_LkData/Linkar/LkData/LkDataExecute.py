from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions
from .LkData import LkData

"""
	Class: LkDataExecute
		Class to management the result of the operations Execute.
		
		Property: Capturing
		string
		
		The Capturing value of the Execute operation.
		
		Property: Returning
		string
		
		The Returning value of the Execute operation
"""
class LkDataExecute(LkData):

	"""
		Constructor: __init__
			Initializes a new instance of the LkDataExecute class.
		
		Arguments:
			executeResult - (string) The string result of the Execute operation execution.
	"""
	def __init__(self, executeResult):
		super().__init__(executeResult)
		self.Capturing = StringFunctions.ExtractCapturing(executeResult)
		self.Returning = StringFunctions.ExtractReturning(executeResult)
		