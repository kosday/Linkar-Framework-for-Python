"""
	Constant: TOTAL_RECORDS_KEY
	The tag value for "TOTAL_RECORDS_KEY" in Database operation responses of MV type.
"""
TOTAL_RECORDS_KEY = "TOTAL_RECORDS"

"""
	Constant: TOTAL_RECORDS
	The tag value for "TOTAL_RECORDS" in Database operation responses of MV type.
"""
RECORD_IDS_KEY = "RECORD_ID"

"""
	Constant: RECORDS_KEY
	The tag value for "RECORDS_KEY" in Database operation responses of MV type.
"""
RECORDS_KEY = "RECORD"

"""
	Constant: CALCULATED_KEY
	The tag value for "CALCULATED_KEY" in Database operation responses of MV type.
"""
CALCULATED_KEY = "CALCULATED"

"""
	Constant: RECORD_DICTS_KEY
	The tag value for "RECORD_DICTS_KEY" in Database operation responses of MV type.
"""
RECORD_DICTS_KEY = "RECORD_DICTS"

"""
	Constant: RECORD_ID_DICTS_KEY
	The tag value for "RECORD_ID_DICTS_KEY" in Database operation responses of MV type.
"""
RECORD_ID_DICTS_KEY = "RECORD_ID_DICTS"

"""
	Constant: CALCULATED_DICTS_KEY
	The tag value for "CALCULATED_DICTS_KEY" in Database operation responses of MV type.
"""
CALCULATED_DICTS_KEY = "CALCULATED_DICTS"

"""
	Constant: ARGUMENTS_KEY
	The tag value for "ARGUMENTS_KEY" in Database operation responses of MV type.
"""
ARGUMENTS_KEY = "ARGUMENTS"

"""
	Constant: ORIGINAL_RECORDS_KEY
	The tag value for "ORIGINAL_RECORDS_KEY" in Database operation responses of MV type.
"""
ORIGINAL_RECORDS_KEY = "ORIGINALRECORD"

"""
	Constant: FORMAT
	The tag value for "FORMAT" in Database operation responses of MV type.
"""
FORMAT_KEY = "FORMAT"

"""
	Constant: CONVERSION
	The tag value for "CONVERSION" in Database operation responses of MV type.
"""
CONVERSION_KEY = "CONVERSION"

"""
	Constant: CAPTURING
	The tag value for "CAPTURING" in Database operation responses of MV type.
"""
CAPTURING_KEY = "CAPTURING"

"""
	Constant: RETURNING
	The tag value for "RETURNING" in Database operation responses of MV type.
"""
RETURNING_KEY = "RETURNING"

"""
	Constant: ROWHEADERS
	The tag value for "ROWHEADERS" in Database operation responses of MV type.
"""
ROWHEADERS_KEY = "ROWHEADERS"

"""
	Constant: ROWPROPERTIES
	The tag value for "ROWPROPERTIES" in Database operation responses of MV type.
"""
ROWPROPERTIES_KEY = "ROWPROPERTIES"

"""
	Constant: ROWPROPERTIES
	The tag value for "ROWPROPERTIES" in Database operation responses of MV type.
"""
ERRORS_KEY = "ERRORS"

"""
	Constant: DC4
	ASCII character used as separator of the arguments of a subroutine.
"""
DC4 = '\u0014'

"""
	Constant: DC4_str
	ASCII character used as separator of the arguments of a subroutine.
"""
DC4_str = "\u0014"

"""
	Constant: FS
	When the responses of the operations are of MV type, this character is used to separate the header (the ThisList property in LkData) from the data.
"""
FS = '\u001C'

"""
	Constant: FS_str
	When the responses of the operations are of MV type, this character is used to separate the header (the ThisList property in LkData) from the data.
"""
FS_str = "\u001C"

"""
	Constant: RS
	ASCII character used by Linkar as separator of items in lists. For example, list of records.
"""
RS = '\u001E'

"""
	Constant: RS_str
	ASCII character used by Linkar as separator of items in lists. For example, list of records.
"""
RS_str = "\u001E"

"""
	Constant: AM
	Character ASCII 253. VM Multi-value mark.
"""
AM = '\u00FE'

"""
	Constant: AM_str
	Character ASCII 253. VM Multi-value mark.
"""
AM_str = "\u00FE"

"""
	Constant: VM
	Character ASCII 253. VM Multi-value mark.
"""
VM = '\u00FD'

"""
	Constant: VM_str
	Character ASCII 253. VM Multi-value mark.
"""
VM_str = "\u00FD"

"""
	Class: StringFunctions
		Set of functions that help manipulate the character strings that are used as input and output data in MV type operations 
"""
class StringFunctions:

	"""
		Function: ExtractTotalRecords
			Looks for the TOTAL_RECORDS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			number
		
		The value of TOTAL_RECORDS_KEY tag.
	"""
	@staticmethod
	def ExtractTotalRecords(lkString):
		block = StringFunctions.GetData(lkString, TOTAL_RECORDS_KEY, FS_str, AM_str)
		try:  
			return int(block)
		except Exception as e:  
			return 0

	"""
		Function: ExtractRecordIds
			Looks for the RECORD_IDS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RECORD_IDS_KEY tag.
	"""
	@staticmethod
	def ExtractRecordIds(lkString):
		valueTag = StringFunctions.GetData(lkString, RECORD_IDS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, RS_str)
	
	"""
		Function: ExtractRecords
			Looks for the RECORDS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RECORDS_KEY tag.
	"""
	@staticmethod
	def ExtractRecords(lkString):
		valueTag = StringFunctions.GetData(lkString, RECORDS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, RS_str)
	
	"""
		Function: ExtractErrors
			Looks for the ERRORS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of ERRORS_KEY tag.
	"""
	@staticmethod
	def ExtractErrors(lkString):
		valueTag = StringFunctions.GetData(lkString, ERRORS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, AM_str)
	
	"""
		Function: FormatError
			This function formats the message error by split into Error Code and Error Message.
		
		Arguments:
			error - (string) The value of ERRORS_KEY tag.
		
		Return:
			string
		
			The error formated.
	"""
	@staticmethod
	def FormatError(error):
		result = error
		items = error.split(VM_str)
		if len(items) == 2:
			result = "ERROR CODE: " + str(items[0]) + " ERROR MESSAGE: " + str(items[1])
		return result
	
	"""
		Function: ExtractRecordsCalculated
			Looks for the CALCULATED_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of CALCULATED_KEY tag.
	"""
	@staticmethod
	def ExtractRecordsCalculated(lkString):
		valueTag = StringFunctions.GetData(lkString, CALCULATED_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, RS_str)
	
	"""
		Function: ExtractRecordsDicts
			Looks for the RECORD_DICTS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RECORD_DICTS_KEY tag.
	"""
	@staticmethod
	def ExtractRecordsDicts(lkString):
		valueTag = StringFunctions.GetData(lkString, RECORD_DICTS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, AM_str)
	
	"""
		Function: ExtractRecordsCalculatedDicts
			Looks for the CALCULATED_DICTS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of CALCULATED_DICTS_KEY tag.
	"""
	@staticmethod
	def ExtractRecordsCalculatedDicts(lkString):
		valueTag = StringFunctions.GetData(lkString, CALCULATED_DICTS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, AM_str)
	
	"""
		Function: ExtractRecordsIdDicts
			Looks for the RECORD_ID_DICTS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RECORD_ID_DICTS_KEY tag.
	"""
	@staticmethod
	def ExtractRecordsIdDicts(lkString):
		valueTag = StringFunctions.GetData(lkString, RECORD_ID_DICTS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, AM_str)
	
	"""
		Function: ExtractOriginalRecords
			Looks for the ORIGINAL_RECORDS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of ORIGINAL_RECORDS_KEY tag.
	"""
	@staticmethod
	def ExtractOriginalRecords(lkString):
		valueTag = StringFunctions.GetData(lkString, ORIGINAL_RECORDS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, RS_str)	

	"""
		Function: ExtractDictionaries
			Looks for the RECORDS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RECORDS_KEY tag.
	"""
	@staticmethod
	def ExtractDictionaries(lkString):
		valueTag = StringFunctions.GetData(lkString, RECORDS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(valueTag, RS_str)
	
	"""
		Function: ExtractConversion
			Looks for the CONVERSION_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of CONVERSION_KEY tag.
	"""
	@staticmethod
	def ExtractConversion(lkString):
		return StringFunctions.GetData(lkString, CONVERSION_KEY, FS_str, AM_str)
	
	"""
		Function: ExtractFormat
			Looks for the FORMAT_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of FORMAT_KEY tag.
	"""
	@staticmethod
	def ExtractFormat(lkString):
		return StringFunctions.GetData(lkString, FORMAT_KEY, FS_str, AM_str)
	
	"""
		Function: ExtractCapturing
			Looks for the CAPTURING_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of CAPTURING_KEY tag.
	"""
	@staticmethod
	def ExtractCapturing(lkString):
		return StringFunctions.GetData(lkString, CAPTURING_KEY, FS_str, AM_str)
	
	"""
		Function: ExtractReturning
			Looks for the RETURNING_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of RETURNING_KEY tag.
	"""
	@staticmethod
	def ExtractReturning(lkString):
		return StringFunctions.GetData(lkString, RETURNING_KEY, FS_str, AM_str)
	
	"""
		Function: ExtractSubroutineArgs
			Looks for the ARGUMENTS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of ARGUMENTS_KEY tag.
	"""
	@staticmethod
	def ExtractSubroutineArgs(lkString):
		arguments = StringFunctions.GetData(lkString, ARGUMENTS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(arguments, DC4_str)

	"""
		Function: ExtractRowProperties
			Looks for the ROWPROPERTIES_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of ROWPROPERTIES_KEY tag.
	"""
	@staticmethod
	def ExtractRowProperties(lkString):
		rowProperties = StringFunctions.GetData(lkString, ROWPROPERTIES_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(rowProperties, AM_str)
	
	"""
		Function: ExtractRowHeaders
			Looks for the ROWHEADERS_KEY tag inside "<lkString>", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
		
		Return:
			string
		
			The value of ROWHEADERS_KEY tag.
	"""
	@staticmethod
	def ExtractRowHeaders(lkString):
		rowHeaders = StringFunctions.GetData(lkString, ROWHEADERS_KEY, FS_str, AM_str)
		return StringFunctions.splitArray(rowHeaders, AM_str)
	
	"""
		Function: GetData
			Looks for the "tag" inside the "lkString", and extracts its value.
		
		Arguments:
			lkString - (string) A string obtained as a result of executing an operation.
			tag - (string) The tag to looking for
			delimiter - (string) Delimiter char of every main items in "lkString".
			delimiterThisList - (string) Delimiter char inside the first item of "lkString". The first item of "lkString" is always the header tags (THISLIST).
		
		Return:
			string
		
			The value of tag.
	"""
	@staticmethod
	def GetData(lkString, tag, delimiter, delimiterThisList):
		block = ""
		parts = lkString.split(delimiter)
		if len(parts) >= 1:
			i = 0
			headersList = parts[0].split(delimiterThisList)
			for header in headersList:
				if tag.upper() == header.upper():
					block = parts[i]
					break
				i += 1
		return block
	
	"""
		Function: splitArray
			Auxiliary function to extract arrays inside a tag value.
		
		Arguments:
			valueTag - (string) The string to be splitted.
			delimiter - (string) The char to use for split.
		
		Return:
			string
		
			The array extracted.
	"""
	@staticmethod
	def splitArray(valueTag, delimiter):
		if valueTag is None or len(valueTag) == 0:
			return []
		else:
			return valueTag.split(delimiter)

	""" Composition Functions """

	"""
		Function: ComposeRecordIds
			Composes the final string of various "recordsIds". Used by CRUD Operations.
		
		Arguments:
			recordIds - (array) Array with the "recordIds" to be joined</param>
		
		Return:
			string
		
			The final string of "recordIds" to be used by CRUD Operations.
	"""
	@staticmethod
	def ComposeRecordIds(recordIds):
		return StringFunctions.JoinArray(recordIds, RS_str)

	"""
		Function: ComposeRecords
			Composes the final string of various "records". Used by CRUD Operations.
		
		Arguments:
			records - (array) Array with the "records" to be joined.
		
		Return:
			string
		
			The final string of "records" to be used by CRUD Operations.
	"""
	@staticmethod
	def ComposeRecords(records):
		return StringFunctions.JoinArray(records, RS_str)
	
	"""
		Function: ComposeOriginalRecords
			Composes the final string of various "originalRecords". Used by CRUD Operations.
		
		Arguments:
			originalRecords - (array) Array with the "originalRecords" to be joined.
		
		Return:
			string
		
			The final string of "originalRecords" to be used by CRUD Operations.
	"""
	@staticmethod
	def ComposeOriginalRecords(originalRecords):
		return StringFunctions.JoinArray(originalRecords, RS_str)
	
	"""
		Function: ComposeDictionaries
			Composes the final string of various "dictionaries". Used by Read and Select Operations.
		
		Arguments:
			dictionaries - (array) Array with the "dictionaries" to be joined.
		
		Return:
			string
		
			The final string of "dictionaries" to be used by Read and Select Operations.
	"""
	@staticmethod
	def ComposeDictionaries(dictionaries):
		return StringFunctions.JoinArray(dictionaries, " ")
	
	"""
		Function: ComposeExpressions
			Composes the final string of various "expressions". Used by Format and Conversion Operations.
		
		Arguments:
			expressions- (array) >Array with the "expressions" to be joined.
		
		Return:
			string
		
			The final string of "expressions" to be used in Format and Conversion Operations.
	"""
	@staticmethod
	def ComposeExpressions(expressions):
		return StringFunctions.JoinArray(expressions, VM_str)	

	"""
		Function: ComposeSubroutineArgs
			Composes the final string of various "arguments" of a subroutine.
		
		Arguments:
			args- (array) >Array with the "arguments" to be joined.
		
		Return:
			string
		
			The final string to be used in Subroutine Operations.
	"""
	@staticmethod
	def ComposeSubroutineArgs(arguments):
		return StringFunctions.JoinArray(arguments, DC4_str)
	
	"""
		Function: JoinArray
			Auxiliary function to compose the final string of multiple items using "delimiter" as separation char.
		
		Arguments:
			items - (array) The "items" to be joined.
			delimiter - (string) The "delimiter" char between the "items".
		
		Return:
			string
		
			The final string with the different items joined by "delimiter" char.
	"""
	@staticmethod
	def JoinArray(items, delimiter):
		if items is not None and len(items) > 0:
			return delimiter.join(items)
		else:
			return ""
	
	"""
		Function: ComposeUpdateBuffer
			Compose the fully buffer of the Update Operations with the block of "recordIds", "records" and "originalRecords".
		
		Arguments:
			recordIds - (string or array) Block of "recordIds". You can obtain this block with <ComposeRecordIds> function or directly using an array.
			records - (string or array) Block of "records". You can obtain this block with <ComposeRecords> function or directly using an array.
			originalRecords - (string or array) Block of "originalRecords". You can obtain this block with <ComposeRecords> function or directly using an array.
		
		Return:
			string
		
		The buffer to be used by Update Operations.
	"""
	@staticmethod
	def ComposeUpdateBuffer(recordIds, records, originalRecords):
		if (isinstance(recordIds, list)):
			if (len(recordIds) != len(records) and originalRecords is None) or (len(recordIds) != len(originalRecords)):
				raise Exception("The arrays must have the same length")
			return FS.join((StringFunctions.ComposeRecordIds(recordIds), StringFunctions.ComposeRecords(records), StringFunctions.ComposeRecords(originalRecords) if originalRecords else ""))
		else:
			return FS.join((recordIds, records, originalRecords if originalRecords else ""))
	
	"""
		Function: ComposeNewBuffer
			Compose the fully buffer of the New Operations with the block of "recordIds" and "records".
		
		Arguments:
			recordIds - (string or array) Block of "recordIds". You can obtain this block with ComposeRecordIds function or directly using an array.
			records (string or array) Block of "records". You can obtain this block with ComposeRecords function or directly using an array.
		
		Return:
			string
		
			The buffer to be used by New Operations.
	"""
	@staticmethod
	def ComposeNewBuffer(recordIds, records):
		if (isinstance(recordIds, list)):
			if (len(recordIds) != len(records)):
				raise Exception("The lists must have the same length")
			return StringFunctions.ComposeRecordIds(recordIds)  + FS +StringFunctions. ComposeRecords(records)
		else:
			return recordIds + FS + records
	
	"""
		Function: ComposeDeleteBuffer
			Compose the fully buffer of the Delete Operations with the block of "recordIds" and "originalRecords".
		
		Arguments:
			recordIds - Block of "recordIds". You can obtain this block with ComposeRecordIds function or directly using an array.
			originalRecords - Block of "originalRecords". You can obtain this block with ComposeRecords function or directly using an array.
		
		Return:
			string
		
			The buffer to be used by Delete Operations.
	"""
	@staticmethod
	def ComposeDeleteBuffer(recordIds, originalRecords):
		if (isinstance(recordIds, list)):
			if originalRecords is not None and len(recordIds) != len(originalRecords):
				raise Exception("The lists must have the same length")	
			return StringFunctions.ComposeRecordIds(recordIds) + FS + StringFunctions.ComposeRecords(originalRecords) if originalRecords else ""
		else:
			return recordIds + FS + (originalRecords if originalRecords else "")
	