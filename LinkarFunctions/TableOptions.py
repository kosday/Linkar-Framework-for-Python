from . import DBMV_Mark
from .SCHEMA_TYPE import SCHEMA_TYPE
from .ROWHEADERS_TYPE import ROWHEADERS_TYPE

"""
	Class: TableOptions
		Detailed options to be used in GetTable and related functions.
		
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
		Property: RepeatValues
			boolean
			
			Repeat common atributes in MV and SV groups.
		Property: ApplyConversion
			boolean
			
			Execute Conversions: With Dictionaries, conversion defined in the dictionary. With Schemas conversions defined in Linkar Schemas.
		Property: ApplyFormat
			boolean
			
			Execute Formats. With Dictionaries, formats defined in the dictionary. With Schemas formats defined in Linkar Schemas.
		Propery: Calculated
			boolean
			
			Return the resulting values from the calculated dictionaries.
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
class TableOptions:
	"""
		Constructor: __init__()
		
		Initializes a new instance of the TableOptions class.
		
		The object is created with the default values for queries with LKSCHEMAS type schemas.
	"""
	def __init__(self):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = False
		self.RowHeader = ROWHEADERS_TYPE.MAINLABEL
		self.RowProperties = False
		self.OnlyVisibles = False
		self.UsePropertyNames = False
		self.RepeatValues = False
		self.ApplyConversion = False
		self.ApplyFormat = False
		self.Calculated = False
		self.Pagination = False
		self.Pagination_RegPage = 10
		self.Pagination_NumPage = 1

	"""
		Function: LkSchemas
			Initializes the instance of the TableOptions class.
			
			Constructor of object used to obtain queries of the LKSCHEMAS schema type.
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			rowProperties - (boolean) First row contains property names.
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			usePropertyNames - (boolean) Use Properties and Table names.
			repeatValues - (boolean) Repeat common atributes in MV and SV groups.
			applyConversion - (boolean) Execute Conversions: With Dictionaries, conversion defined in the dictionary. With Schemas conversions defined in Linkar Schemas.
			applyFormat - (boolean) Execute Formats. With Dictionaries, formats defined in the dictionary. With Schemas formats defined in Linkar Schemas.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def LkSchemas(self, rowHeader=ROWHEADERS_TYPE.MAINLABEL, rowProperties=False, onlyVisibles=False, usePropertyNames=False, repeatValues=False, applyConversion=False, applyFormat=False, calculated=False, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = rowProperties
		self.OnlyVisibles = onlyVisibles
		self.UsePropertyNames = usePropertyNames
		self.RepeatValues = repeatValues
		self.ApplyConversion = applyConversion
		self.ApplyFormat = applyFormat
		self.Calculated = calculated
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: SqlMode
			Initializes the instance of the TableOptions class.
			
			Constructor of object used to perform queries of the SQLMODE type schemas.
		Arguments:
			onlyVisibles - (boolean) Use only Visible Schemas and Properties.
			applyConversion - (boolean) Execute Conversions: With Dictionaries, conversion defined in the dictionary. With Schemas conversions defined in Linkar Schemas.
			applyFormat - (boolean) Execute Formats. With Dictionaries, formats defined in the dictionary. With Schemas formats defined in Linkar Schemas.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def SqlMode(self, onlyVisibles=False, applyConversion=False, applyFormat=False, calculated=False, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.LKSCHEMAS
		self.SqlMode = True
		self.RowHeader = ROWHEADERS_TYPE.NONE
		self.RowProperties = True
		self.OnlyVisibles = onlyVisibles
		self.UsePropertyNames = True
		self.RepeatValues = True
		self.ApplyConversion = applyConversion
		self.ApplyFormat = applyFormat
		self.Calculated = calculated
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: Dictionaries
			Initializes the instance of the TableOptions class.
			
			Constructor of object used to perform queries of the DICTIONARIES type schemas.
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			repeatValues - (boolean) Repeat common atributes in MV and SV groups.
			applyConversion - (boolean) Execute Conversions: With Dictionaries, conversion defined in the dictionary. With Schemas conversions defined in Linkar Schemas.
			applyFormat - (boolean) Execute Formats. With Dictionaries, formats defined in the dictionary. With Schemas formats defined in Linkar Schemas.
			calculated - (boolean) Return the resulting values from the calculated dictionaries.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.
	"""
	def Dictionaries(self, rowHeader=ROWHEADERS_TYPE.MAINLABEL, repeatValues=False, applyConversion=False, applyFormat=False, calculated=False, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.DICTIONARIES
		self.SqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = False
		self.OnlyVisibles = False
		self.UsePropertyNames = False
		self.RepeatValues = repeatValues
		self.ApplyConversion = applyConversion
		self.ApplyFormat = applyFormat
		self.Calculated = calculated
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage


	"""
		Function: None
			Initializes the instance of the TableOptions class.
			
			Constructor of object used to perform queries without schema information.
		Arguments:
			rowHeaders - (<ROWHEADERS_TYPE>) Include headings in first row MAINLABEL (main headings), SHORTLABEL (short label headings), and NONE (without headings).
			repeatValues - (boolean) Repeat common atributes in MV and SV groups.
			pagination - (boolean) True if pagination is being used.
			regPage - (number) For use with pagination, indicates the number of records by page. Must be greater than 0.
			numPage - (number) For use with pagination, indicates the page number to obtain. Must be greater than 0.

	"""
	def None(self, rowHeader=ROWHEADERS_TYPE.MAINLABEL, repeatValues=False, pagination=False, regPage=10, numPage=1):
		self.SchemaType = SCHEMA_TYPE.NONE
		self.SqlMode = False
		self.RowHeader = rowHeader
		self.RowProperties = False
		self.OnlyVisibles = False
		self.UsePropertyNames = False
		self.RepeatValues = repeatValues
		self.ApplyConversion = False
		self.ApplyFormat = False
		self.Calculated = False
		self.Pagination = pagination
		self.Pagination_RegPage = regPage
		self.Pagination_NumPage = numPage



	"""
		Function: GetString
			Composes the GetTable options string for processing through LinkarSERVER to the database.
			
		Returns:
			string
			
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		str_a = DBMV_Mark.AM_str.join([
			self.SchemaType,
			"1" if self.SqlMode else "0",
			"1" if self.UsePropertyNames else "0",
			"1" if self.RowProperties else "0",
			"1" if self.OnlyVisibles else "0",
			self.RowHeader,
			"1" if self.RepeatValues else "0",
			"1" if self.ApplyConversion else "0",
			"1" if self.ApplyFormat else "0",
			"1" if self.Calculated else "0"
		])

		str_b = DBMV_Mark.VM_str.join([
			"1" if self.Pagination else "0",
			self.Pagination_RegPage,
			self.Pagination_NumPage
		])
		return str_a + DBMV_Mark.AM_str + str_b