from .DBMV_Mark import DBMV_Mark

"""
	Class: RecoverIdType
		Object that works as an argument in <DeleteOptions> function and defines the technique for recovering deleted item IDs.
		
	Property: ActiveTypeLinkar
		boolean
		
		Indicates that the RecoverIdType *Linkar* is enabled.
	Property: ActiveTypeCustom
		boolean
		
		Indicates that the RecoverIdType *Custom* is enabled.
	Property: Prefix
		string
		
		(For RecoverIdType *Linkar*)
		A prefix to the code.
	Property: Separator
		string
		
		(For RecoverIdType *Linkar*)
		The separator between the prefix and the code.
		The allowed separators list is: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~.
"""
class RecoverIdType:
	ActiveTypeLinkar = False
	Prefix = ""
	Separator = ""
	
	ActiveTypeCustom = False
	
	"""
		Constructor: __init__
			No id recovery technique will be used.
	"""
	def __init__(self):
		pass

	"""
		Function: Linkar
			Use this constructor for recovering items ids that used *Linkar* <RecordIdType>.
		
		Arguments:
			prefix - (string) Adding a prefix to the item ID.
			separator - (string) The separator between the prefix and the ID. Valid delimiters: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
	"""
	def Linkar(self, prefix, separator):
		self.ActiveTypeLinkar = True
		self.Prefix = prefix
		self.Separator = separator

	"""
		Function: Custom
			Use this function to recovering items ids that used *Custom* RecordIdType.
	"""
	def Custom(self):
		self.ActiveTypeCustom = True

	"""
		Function: GetStringAM
			Composes the RecoverIdType options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
			
			The string ready to be used by LinkarSERVER.
	"""
	def GetStringAM(self):
		if self.ActiveTypeLinkar:
			opLinkar = "1" + DBMV_Mark.VM_str + self.Prefix + DBMV_Mark.VM_str + self.Separator
		else:
			opLinkar = "0" + DBMV_Mark.VM_str + "" + DBMV_Mark.VM_str + ""

		opCustom = "1" if self.ActiveTypeCustom else "0"
		return opLinkar + DBMV_Mark.AM_str + opCustom
		