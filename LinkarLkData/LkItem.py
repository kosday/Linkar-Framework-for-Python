import numbers
from LinkarStrings import StringFunctions
from LinkarFunctions.MvOperations import MvOperations

"""
	Class: LkItem
		A LkItem is compose of three items: RecordId, Record and OriginalRecord. Depending on the operation, the three items may be present, or only some of them.
		Each LkItem can hold a list of dictionaries (for real fields, for ID fields, and for calculated fields)
		
		Property: RecordId
		string
		
		The ID of the record.
		
		Property: Record
		string
		
		The content of a record from database.
		
		Property: OriginalRecord
		string
		
		A copy of the original record to be used in operations where the optimistic lock option is enabled.
		
		Property Calculated
		string
		
		The content of calculated fields from database.
		
		Property: LstDictsId
		string array
		
		Array with the dictionary names for record Ids.
		
		Property: LstDicts
		string array
		
		Array with the dictionary names for record fields.
		
		Property: LstDictsCalculated
		string array
		
		Array with the dictionary names for calculated fields of the record.
"""
class LkItem:

	"""
		Constructor: __init__()
			Initializes a new instance of the LkItem class.
			
		Arguments:
			recordId - (string) The ID of the record.
			record - (string) The content of a record from database.
			calculateds - (string) The content of the calculated fields of the records.
			originalRecord - (string) A copy of the original record to be used in operations where the optimistic lock option is enabled.
			lstDictsId - (string array) Optionally, array with the dictionary names for record Ids.
			lstDicts - (string array) Optionally, array with the dictionary names for record fields.
			lstDictsCalculated - (string array) Optionally, array with the dictionary names for calculated fields of the record.
	"""
	def __init__(self, recordId = "", record = "", calculateds = "", originalRecord = "", lstDictsId = [], lstDicts = [], lstDictsCalculated = []):
		self.RecordId = recordId
		self.Record = record
		self.OriginalRecord = originalRecord
		self.Calculated = calculateds
		self.LstDictsId = lstDictsId
		self.LstDicts = lstDicts
		self.LstDictsCalculated = lstDictsCalculated
	

	"""
		Function: get
			Get attribute (fields number or dictionary names), multivalues or subvalues from the record.
			
		Arguments:
			attribute - (number or string) The field number or dictionary name to get.
			mv - (number) The multivalue number to get.
			sv - (number) The subvalue number to get.
			
		Returns:
			string
			
			The extrated value.
	"""
	def get(self, attribute, mv = 0, sv = 0):
		if isinstance(attribute, numbers.Number):
			return MvOperations.LkExtract(self.Record, attribute, mv, sv)
		else:
			for i in range(len(self.LstDictsId)):
				if self.LstDictsId[i] == attribute:
					return self.RecordId
			
			for i in range(len(self.LstDicts)):
				if self.LstDicts[i] == attribute:
					return MvOperations.LkExtract(self.Record, (i + 1), mv, sv)

			for i in range(len(self.LstDictsCalculated)):
				if self.LstDictsCalculated[i] == attribute:
					return MvOperations.LkExtract(self.Calculated, (i + 1), mv, sv)
				
			raise Exception("Dictionary name not found")
		
	

	"""
		Function: set
			Set attribute (fields number or dictionary names), multivalues or subvalues from the record.
			
		Arguments:
			attribute - (number or string) The field number or dictionary name to set.
			mv - (number) The multivalue number to set.
			sv - (number) The subvalue number to set.
	"""
	def set(self, value, attribute, mv = 0, sv = 0):
		if isinstance(attribute, numbers.Number):
			self.Record = MvOperations.LkReplace(self.Record, value, attribute, mv, sv)
		else:
			if len(self.LstDictsId) == 0:
				raise Exception("Dictionaries ID List Empty")

			for i in range(len(self.LstDictsId)):
				if self.LstDictsId[i] == attribute:
					self.RecordId = value
					return
				
			if len(self.LstDictsId) == 0:
				raise Exception("Dictionaries List Empty")

			for i in range(len(self.LstDicts)):
				if (self.LstDicts[i] == attribute):
					self.Record = MvOperations.LkReplace(self.Record, value, (i + 1), mv, sv)
					return
				
			raise Exception("Dictionary name not found")
		
	

	"""
		Function: ComposeReadBuffer
			Composes the final buffer string for one or more records to be read in MV Read operations, with the RecordId information.
		
		Returns:
		string
		
		The final string buffer for MV Read operations.
	"""
	def ComposeReadBuffer(self):
		return self.RecordId
	

	"""
		Function: ComposeUpdateBuffer
			Composes the final buffer string for one or more records to be updated in MV Update operations, with the RecordId, the Record, and optionally the OriginalRecord information.
			
		Arguments:
			includeOriginalBuffer - (boolean) Determines if the OriginalRecord must be include or not in the final buffer string.
		
		Returns:
		string
		
		The final string buffer for MV Update operations.
	"""
	def ComposeUpdateBuffer(self, includeOriginalBuffer = False):
		if includeOriginalBuffer:
			return StringFunctions.ComposeUpdateBuffer(self.RecordId, self.Record, self.OriginalRecord)
		else:
			return StringFunctions.ComposeUpdateBuffer(self.RecordId, self.Record)
	

	"""
		Function: ComposeNewBuffer
			Composes the final buffer string for one or more records to be created in MV New operations, with the RecordId and the Record information.
		
		Returns:
		string
		
		The final string buffer for MV New operations.
	"""
	def ComposeNewBuffer(self):
		return StringFunctions.ComposeNewBuffer(self.RecordId, self.Record)
	

	"""
		Function: ComposeDeleteBuffer
			Composes the final buffer string for one or more records to be deleted in MV Delete operations, with the RecordId and optionally with the OriginalRecord information.
			
		Arguments:
			includeOriginalBuffer - (boolean) Determines if the OriginalRecord must be include or not in the final buffer string.
		
		Returns:
		string
		
		The final string buffer for MV Delete operations.
	"""
	def ComposeDeleteBuffer(self, includeOriginalBuffer = False):
		if includeOriginalBuffer:
			return StringFunctions.ComposeDeleteBuffer(self.RecordId, self.OriginalRecord)
		else:
			return StringFunctions.ComposeDeleteBuffer(self.RecordId)
	