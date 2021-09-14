from .DBMV_Mark import DBMV_Mark
from .SCHEMA_TYPE import SCHEMA_TYPE
from .ROWHEADERS_TYPE import ROWHEADERS_TYPE

"""
	Class: LkSchemasOptions
		Contains the options to obtain different types of schemas with the LkSchemas function.
		
		Property: SchemaType
			<SCHEMA_TYPE>
			
			Indicates the type of LkSchemas used.
		Property: RowHeaders
			<ROWHEADERS_TYPE>
			
			Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
		Property: SqlMode
			boolean
			
			SQLMODE type schemas
		Property: RowProperties
			boolean
			First row contains property names.
		Property: OnlyVisibles
			boolean
			
			Use only Visible Schemas and Properties.
		Property: Pagination
			boolean
			
			Indicates if pagination is being used or not.
		Property: Pagination_RegPage
			number
			
			In case of pagination indicates the number of records by page. It must be bigger than 0.
		Property: Pagination_NumPage
			number
			
			In case of pagination it indicates the page number to obtain. Must be greater than 0
"""
class LkSchemasOptions:
	"""
		Constructor: __init__
			Initializes a new instance of the LkSchemasOptions class.
			
			The object is created with the default values for LKSCHEMAS type schemas.
	"""
	def __init__(self):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.IsSqlMode = False
		self.RowHeader = ROWHEADERS_TYPE.MAINLABEL
		self.RowProperties = False
		self.OnlyVisibles = False
		self.Pagination = False
		self.Pagination_RegPage = 10
		self.Pagination_NumPage = 1


	"""
		Function: LkSchemas
			Constructor of object used to obtain LKSCHEMAS type schemas.
			
			Initializes a new instance of the LkSchemasOptions class.
		
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			rowProperties - (boolean) First row contains property names.
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def LkSchemas(self, rowHeader=ROWHEADERS_TYPE.MAINLABEL, rowProperties=False, onlyVisibles = False, pagination = False, regPage = 10, numPage = 1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.IsSqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = rowProperties
		self.OnlyVisibles = onlyVisibles
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: SqlMode
			Initializes the instance of the LkSchemasOptions class.
			Constructor of object used to obtain SQLMODE type schemas. Creation options are allowed for SQLMODE type schemas.
		
		Arguments:
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def SqlMode(self, onlyVisibles=False, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.IsSqlMode = True
		self.RowHeader = ROWHEADERS_TYPE.NONE
		self.RowProperties = True
		self.OnlyVisibles = onlyVisibles
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: Dictionaries
			Initializes the instance of the LkSchemasOptions class.
			
			Constructor of object used to obtain DICTIONARIES type schemas. Creation options are allowed for DICTIONARIES type schemas.
		
		Arguments:
			rowHeaders - (ROWHEADERS_TYPE) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def Dictionaries(self, rowHeader=ROWHEADERS_TYPE.MAINLABEL, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.DICTIONARIES
		self.IsSqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = True
		self.OnlyVisibles = True
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: GetString
			Composes the LkSchemas options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
		
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		return str(self.SchemaType) + DBMV_Mark.AM_str + ("1" if self.IsSqlMode else "0") + DBMV_Mark.AM_str + ("1" if self.RowProperties else "0") + DBMV_Mark.AM_str + ("1" if self.OnlyVisibles else "0") + DBMV_Mark.AM_str + str(self.RowHeader) + DBMV_Mark.AM_str + ("1" if self.Pagination else "0") + DBMV_Mark.VM_str + str(self.Pagination_RegPage) + DBMV_Mark.VM_str + str(self.Pagination_NumPage)