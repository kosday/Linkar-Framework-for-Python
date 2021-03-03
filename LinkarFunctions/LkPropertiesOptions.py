from . import DBMV_Mark
from .SCHEMA_TYPE import SCHEMA_TYPE
from .ROWHEADERS_TYPE import ROWHEADERS_TYPE

"""
	Class: LkPropertiesOptions
		Contains the options to obtain the list of Properties of the different types of schemas with the LkProperties function.
		
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
		Property: UsePropertyNames
			boolean
			
			Use Properties and Table names.
		Property: Pagination
			boolean
			
			Indicates if pagination is being used or not.
		Property: Pagination_RegPage
			number
			
			In case of pagination indicates the number of records by page. It must be bigger than 0.
		Property Pagination_NumPage
			number
			
			In case of pagination it indicates the page number to obtain. Must be greater than 0.
"""
class LkPropertiesOptions:
	"""
		Constructor: constructor
			Initializes a new instance of the LkPropertiesOptions class.
			
			The object is created with the default values for list of Schema Properties of LKSCHEMAS type.
	"""
	def __init__(self):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = False
		self.RowHeader = ROWHEADERS_TYPE.MAINLABEL
		self.RowProperties = False
		self.OnlyVisibles = False
		self.UsePropertyNames = False
		self.Pagination = False
		self.Pagination_RegPage = 10
		self.Pagination_NumPage = 1

	"""
		Function: LkSchemas
			Initializes the instance of the LkPropertiesOptions class.
			
			Constructor of object used to obtain a list of Properties of the LKSCHEMAS schema type.
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			rowProperties - (boolean) First row contains property names.
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			usePropertyNames - (boolean) Use Properties and Table names.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def LkSchemas(self, rowHeader = ROWHEADERS_TYPE.MAINLABEL, rowProperties = False, onlyVisibles = False, usePropertyNames = False, pagination = False, regPage = 10, numPage = 1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = rowProperties
		self.OnlyVisibles = onlyVisibles
		self.UsePropertyNames = usePropertyNames
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: SqlMode
			Initializes the instance of the LkPropertiesOptions class.
			
			Constructor of object used to obtain a list of Properties of the SQLMODE schema type.
		Arguments:
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def SqlMode(self, onlyVisibles = False, pagination = False, regPage = 10, numPage = 1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = True
		self.RowHeader = ROWHEADERS_TYPE.NONE
		self.RowProperties = True
		self.OnlyVisibles = onlyVisibles
		self.UsePropertyNames = True
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: Dictionaries
			Initializes the instance of the LkPropertiesOptions class.
			
			Constructor of object used to obtain a list of Properties of the DICTIONARIES schema type.
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>)Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0
	"""
	def Dictionaries(self, rowHeader = ROWHEADERS_TYPE.MAINLABEL, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.DICTIONARIES
		self.SqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = True
		self.OnlyVisibles = True
		self.UsePropertyNames = False
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: GetString
			Composes the LkProperties options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
			
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		return self.SchemaType + DBMV_Mark.AM_str + "1" if self.SqlMode else "0" + DBMV_Mark.AM_str + "1" if self.UsePropertyNames else "0" + DBMV_Mark.AM_str +	"1" if self.RowProperties else "0" + DBMV_Mark.AM_str +	"1" if self.OnlyVisibles else "0" + DBMV_Mark.AM_str + self.RowHeader + DBMV_Mark.AM_str + "1" if self.Pagination else "0" + DBMV_Mark.VM_str + self.Pagination_RegPage + DBMV_Mark.VM_str + self.Pagination_NumPage