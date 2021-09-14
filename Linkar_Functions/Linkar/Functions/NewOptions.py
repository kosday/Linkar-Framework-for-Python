from .DBMV_Mark import DBMV_Mark
from .ReadAfterCommonOptions import ReadAfterCommonOptions
from .RecordIdType import RecordIdType

"""
	Class: NewOptions
		Object that works as an argument in New function and defines the function options.
	
	Property: ActiveTypeLinkar
		boolean
		
		Indicates that the RecordIdType *Linkar* is enabled.
		
	Property: ActiveTypeRandom
		boolean
		
		Indicates that the RecordIdType *Random* is enabled.
	
	Property ActiveTypeCustom
		boolean
		
		Indicates that the RecordIdType *Custom* is enabled.
		
	Property: Prefix
		string
		
		(For RecoverIdType *Linkar*)
		A prefix to the code
		
	Property: Separator
		string
		
		(For RecoverIdType *Linkar*)
		The separator between the prefix and the code.
		The allowed separators list is: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
	Property: FormatSpec
		string
		
		(For RecoverIdType *Linkar*)
		The code format, under the Database syntax.
		
	Property: Numeric
		boolean
		
		(For RecoverIdType *Random*)
		 Indicates if the code must be numeric.
		 
	Property: Length
		number
		
		(For RecoverIdType *Random*)
		Length of the code to create. It must be bigger than 0.
"""
class NewOptions:
	"""
		Constructor: __init__
			Initializes a new instance of the NewOptions class.
			
		Arguments:
			recordIdType - (<RecordIdType>) Specifies the technique for generating item IDs. Mandatory if no registration codes are indicated in the New functions.
			readAfter - (boolean) Reads the record again and returns it after the update. Calculated, conversion, formatSpec and originalRecords will only be applied if this option is true.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			conversion - (boolean) Execute the defined conversions in the dictionaries before returning.
			formatSpec - (boolean) Execute the defined formats in the dictionaries before returning.
			originalRecords- (boolean) Return a copy of the records in MV format.
	"""
	def __init__(self, recordIdType=RecordIdType(), readAfter=False, calculated=False, conversion=False, formatSpec=False, originalRecords=False):
		self.RecordIdType = recordIdType
		if not self.RecordIdType:
			self.RecordIdType = RecordIdType()

		self.ActiveTypeLinkar = self.RecordIdType.ActiveTypeLinkar
		self.Prefix = self.RecordIdType.Prefix
		self.Separator = self.RecordIdType.Separator
		self.FormatSpec = self.RecordIdType.FormatSpec
		self.ActiveTypeRandom = self.RecordIdType.ActiveTypeRandom
		self.Numeric = self.RecordIdType.Numeric
		self.Length = self.RecordIdType.Length
		self.ActiveTypeCustom = self.RecordIdType.ActiveTypeCustom

		if readAfter:
			self.ReadAfterCommonOptions = ReadAfterCommonOptions(readAfter, calculated, conversion, formatSpec, originalRecords)
		else:
			self.ReadAfterCommonOptions = ReadAfterCommonOptions(readAfter, False, False, False, False)

		self.ReadAfter = self.ReadAfterCommonOptions.ReadAfter
		self.Calculated = self.ReadAfterCommonOptions.Calculated
		self.Conversion = self.ReadAfterCommonOptions.Conversion
		self.FormatSpec = self.ReadAfterCommonOptions.FormatSpec
		self.OriginalRecords = self.ReadAfterCommonOptions.OriginalRecords


	"""
		Function: GetString
			Composes the New options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
		
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		return self.RecordIdType.GetStringAM() + DBMV_Mark.AM_str + self.ReadAfterCommonOptions.GetStringAM()