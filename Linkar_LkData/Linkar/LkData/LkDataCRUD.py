from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions
from .LkData import LkData
from .LkItem import LkItem
from .LkItems import LkItems

"""
	Class: LkDataCRUD
		Class to management the result of the operations Read, Update, New, Delete, Select and Dictionaries.
		
		Property: TotalItems
		(number)
		
		Number of the items.
		
		Property: LkRecords
		(<LkItems>)
		
		LkItem list from the CRUD operation execution.
		
"""
class LkDataCRUD(LkData):

	"""
		Constructor: __init__
			Initializes a new instance of the LkDataCRUD class.
			
		Arguments:
			crudOperationResult - (string) The string result of the CRUD operation execution.
	"""
	def __init__(self, crudOperationResult):
		super().__init__(crudOperationResult)
		self.TotalItems = StringFunctions.ExtractTotalRecords(crudOperationResult)
		lstIdDicts = StringFunctions.ExtractRecordsIdDicts(crudOperationResult)
		lstDictionaries = StringFunctions.ExtractRecordsDicts(crudOperationResult)
		lstCalculatedDicts = StringFunctions.ExtractRecordsCalculatedDicts(crudOperationResult)
		self.LkRecords = LkItems(lstIdDicts, lstDictionaries, lstCalculatedDicts)

		lstRecords = StringFunctions.ExtractRecords(crudOperationResult)
		lstRecordIds = StringFunctions.ExtractRecordIds(crudOperationResult)
		lstOriginalRecords = StringFunctions.ExtractOriginalRecords(crudOperationResult)
		lstRecordsCalculated = StringFunctions.ExtractRecordsCalculated(crudOperationResult)
		length = len(lstRecordIds)
		for i in range(length):
			record = lstRecords[i] if length == len(lstRecords) else ""
			originalRecord = lstOriginalRecords[i] if length == len(lstOriginalRecords) else ""
			calculateds = lstRecordsCalculated[i] if length == len(lstRecordsCalculated) else ""		
			lkRecord = LkItem(lstRecordIds[i], record, calculateds, originalRecord)
			self.LkRecords.push(lkRecord)
