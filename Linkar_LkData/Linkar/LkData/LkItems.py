import numbers
from Linkar_Functions.Linkar.Functions import LinkarFunctions
from .LkItem import LkItem

"""
	Class: LkItems
			This class is to implement List of the <LkItem> elements.
			
		Property: LstDictsId
		string array
		
		Array with the dictionary names for record Ids.
		The same array for each LkItem that is stored in the list.
		Property: LstDicts
		string array
		
		Array with the dictionary names for record fields.
		The same array for each LkItem that is stored in the list.
		
		Property: LstDictsCalculated
		string array
		
		Array with the dictionary names for calculated fields of the record.
		The same array for each LkItem that is stored in the list.
"""
class LkItems(list):

	"""
		Constructor: __init__
			Initializes a new instance of the LkItem class.
			
		Arguments:
			lstDictsId - (string array) Array with the dictionary names for record Ids. The same array for each LkItem that is stored in the list.</param>
			lstDicts - (string array) Array with the dictionarty names for record fields. The same array for each LkItem that is stored in the list.</param>
			lstDictsCalculated - (string array) Array with the dictionary names for calculated fields of the record. The same array for each LkItem that is stored in the list.</param>
	"""
	def __init__(self, lstDictsId = [], lstDicts = [], lstDictsCalculated = []):
		##self.LkItems = []
		####self = []
		list.__init__(self)
		self.LstDictsId = lstDictsId
		self.LstDicts = lstDicts
		self.LstDictsCalculated = lstDictsCalculated
		

	def initialize(self, lstDictsId = [], lstDicts = [], lstDictsCalculated = []):
		self.LstDictsId = lstDictsId
		self.LstDicts = lstDicts
		self.LstDictsCalculated = lstDictsCalculated

	"""
		Function: get
			Get a <LkItem> using its RecordId.
			
		Arguments:
			id - (string) The record Id of the LkItem.
		
		Return:
			<LkItem>
			
			The LkItem extracted.
		
	"""
	def get(self, record_id):
		if isinstance(record_id, numbers.Number):
			return self[record_id]
		else:
			for i in range(len(self)):
				if self[i].RecordId == record_id:
					return self[i]
			return None

	"""
		Function: push
			Adds a new LkItem to the list. The dictionaries arrays of the list, will be copied to the LkItem added.
			
		Arguments:
			lkItem - (LkItem) The LkItem to be added.
	"""
	def push(self, lkItem):
		duplicateIds = [x for x in self if x.RecordId == lkItem.RecordId]
		if lkItem.RecordId and len(duplicateIds) == 0:
			lkItem.LstDictsId = self.LstDictsId
			lkItem.LstDicts = self.LstDicts
			lkItem.LstDictsCalculated = self.LstDictsCalculated
			self.append(lkItem)

	"""
		Function: pushId
			Creates and adds LkItem with specific recordIds to the list.
			
		Arguments:
			recordIds - (string array) Array with the list of recordIds.
	"""
	def pushIds(self, recordIds): # Python-List
		for i in range(len(recordIds)):
			lkRecord = LkItem(recordIds[i])
			self.append(lkRecord)
		 
	"""
		Function: removeId
			Removes the LkItem specified by its recordID from the list.
			
		Arguments:
			recordId - (string) The recordId of the LkItem to be removed.
	"""
	def removeId(self, recordId):
		for i in range(len(self)):
			if self[i].RecordId == recordId:
				self.pop(i)
				break
			
	"""
		Function: ComposeReadBuffer
			Composes the final buffer string for one or more records to be read in MV Read operations, with the RecordId information.
			
		Returns:
		string
		
		The final string buffer for MV Read operations.
	"""
	def ComposeReadBuffer(self):
		buf = ""
		for i in range(len(self)):
			if i > 0:
				buf += LinkarFunctions.ASCII_Chars.RS_chr
			buf += self[i].RecordId
		return buf

	"""
		Function: ComposeUpdateBuffer
			Composes the final buffer string for one or more records to be updated in MV Update operations, with the RecordId, the Record,
			and optionally the OriginalRecord information.
			
		Arguments:
			includeOriginalBuffer - (boolean) Determines if the OriginalRecord must be include or not in the final buffer string.
			
		Returns:
		string
		
		The final string buffer for MV Update operations.
	"""
	def ComposeUpdateBuffer(self, includeOriginalBuffer = False):
		buf = ""
		for i in range(len(self)):
			if i > 0:
				buf += LinkarFunctions.ASCII_Chars.RS_chr
			buf += self[i].RecordId
	
		buf += LinkarFunctions.ASCII_Chars.FS_chr
	
		for i in range(len(self)):
			if i > 0:
				buf += LinkarFunctions.ASCII_Chars.RS_chr
			buf += self[i].Record
			
		if includeOriginalBuffer:
			buf += LinkarFunctions.ASCII_Chars.FS_chr
			for i in range(len(self)):
				if i > 0:
					buf += LinkarFunctions.ASCII_Chars.RS_chr
				buf += self[i].OriginalRecord
		return buf
	
	"""
		Function: ComposeNewBuffer
			Composes the final buffer string for one or more records to be created in MV New operations, with the RecordId and the Record information.
		
		Returns:
		string
		
		The final string buffer for MV New operations.
	"""
	def ComposeNewBuffer(self):
		return self.ComposeUpdateBuffer(False)

	"""
		Function: ComposeDeleteBuffer
			Composes the final buffer string for one or more records to be deleted in MV Delete operations, with the RecordId,
			and optionally with the OriginalRecord information.
			
		Arguments:
			includeOriginalBuffer - (boolean) Determines if the OriginalRecord must be include or not in the final buffer string.
			
		Returns:
		string
		
		The final string buffer for MV Delete operations.
	"""
	def ComposeDeleteBuffer(self, includeOriginalBuffer = False):
		buf = ""
		for i in range(len(self)):
			if (i > 0):
				buf += LinkarFunctions.ASCII_Chars.RS_chr
			buf += self[i].RecordId

		if includeOriginalBuffer:
			buf += LinkarFunctions.ASCII_Chars.FS_chr
			for i in range(len(self)):
				if i > 0:
					buf += LinkarFunctions.ASCII_Chars.RS_chr
				buf += self[i].OriginalRecord
		return buf
	