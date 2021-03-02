from . import DBMV_Mark
from . import ASCII_Chars
from .CONVERSION_TYPE import CONVERSION_TYPE
from .ReadOptions import ReadOptions
from .UpdateOptions import UpdateOptions
from .NewOptions import NewOptions
from .DeleteOptions import DeleteOptions
from .SelectOptions import SelectOptions


class OperationArguments:

	"""
		Function: GetReadArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the Read operation.

		Arguments:
			filename - (string) File name to read.
			recordIds - (string) A list of item IDs to read, separated by the Record Separator character (30). Use StringFunctions.ComposeRecordIds to compose this string.
			dictionaries - (string) List of dictionaries to read, separated by space. If this list is not set, all fields are returned.
			readOptions - (<ReadOptions>) Object that defines the different reading options of the Function: Calculated, dictClause, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	
	@staticmethod
	def GetReadArgs(filename, recordIds, dictionaries, readOptions, customVars):
		if not readOptions:
			readOptions = ReadOptions()

		options = readOptions.GetString()
		inputData = filename + DBMV_Mark.AM + recordIds + DBMV_Mark.AM + dictionaries
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData;


	@staticmethod
	def GetSelectArgs(filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions, customVars):
		if not selectOptions:
			selectOptions = SelectOptions()

		options = selectOptions.GetString()
		inputData = filename + DBMV_Mark.AM + selectClause + DBMV_Mark.AM + sortClause + DBMV_Mark.AM + dictClause + DBMV_Mark.AM + preSelectClause
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData