from LinkarStrings import StringFunctions
from .LkData import LkData


"""
	Class: LkDataSchProp
		Class to management the result of the operations LkSchemas and LkProperties.
		
		Property: RowProperties
		string
		
		The RowProperties value of the LkSchemas or LkLkProperties operations.
		
		Property: RowHeaders
		string
		
		The RowHeaders value of the LkSchemas or LkProperties operations.
"""
class LkDataSchProp(LkData):

	"""
		Constructor: __init__()
			Initializes a new instance of the LkDataSchProp class.
		
		Arguments:
			lkSchemasResult - (string) The string result of the Lkchemas or LkProperties operation execution.
	"""
	def __init__(self, lkSchemasResult):
		super().__init__(lkSchemasResult)
		self.RowProperties = StringFunctions.ExtractRowProperties(lkSchemasResult)
		self.RowHeaders = StringFunctions.ExtractRowHeaders(lkSchemasResult)