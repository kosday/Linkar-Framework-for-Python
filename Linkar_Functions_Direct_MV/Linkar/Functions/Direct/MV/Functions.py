from Linkar_Functions_Direct.Linkar.Functions.Direct.DirectFunctions import DirectFunctions
from Linkar_Functions.Linkar.Functions import LinkarFunctions

"""
	class: Functions
		These functions perform direct (without establishing permanent session) operations with output format type MV.
"""
class Functions:

	"""
		Function: Read
			Reads one or several records of a file, with MV input and output format.
			
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) File name to read.
			recordIds - (string) A list of item IDs to read, separated by the Record Separator character (30). Use <StringFunctions.ComposeRecordIds> to compose this string
			dictionaries - (string) List of dictionaries to read, separated by space. If this list is not set, all fields are returned. You may use the format LKFLDx where x is the attribute number.
			readOptions - (<ReadOptions>) Object that defines the different reading options of the Function: Calculated, dictClause, conversion, formatSpec, originalRecords.
			customVars - (string)Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.

		Returns:
			string
		
			The results of the operation.
			
		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyRead():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Read(credentials, "LK.CUSTOMERS","2")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Read(credentialOptions, filename, recordIds, dictionaries="", readOptions=  LinkarFunctions.ReadOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.Read(credentialOptions,filename, recordIds, dictionaries, readOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Update
			Update one or several records of a file, with MV input and output format.
			
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords. Use <StringFunctions.ComposeUpdateBuffer> (Linkar.Strings library) function to compose this string.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.

		Returns:
			string
		
			The results of the operation.
			
		Remarks:
		Inside the records argument, the recordIds and the modified records always must be specified. But the originalRecords not always.
		When <UpdateOptions> argument is specified and the <UpdateOptions.OptimisticLockControl> property is set to true, a copy of the record must be provided before the modification (originalRecords argument)
		to use the Optimistic Lock technique. This copy can be obtained from a previous <Read> operation. The database, before executing the modification, 
		reads the record and compares it with the copy in originalRecords, if they are equal the modified record is executed.
		But if they are not equal, it means that the record has been modified by other user and its modification will not be saved.
		The record will have to be read, modified and saved again.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions.Linkar.Functions import LinkarFunctions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyUpdate():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Update(credentials, "LK.CUSTOMERS",
									"2" + LinkarFunctions.ASCII_Chars.FS_str +							# RecordId
									"CUSTOMER 2þADDRESS 2þ444" + LinkarFunctions.ASCII_Chars.FS_chr +	# Record
									""																	# OriginalRecord
								)

				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Update(credentialOptions, filename, records, updateOptions=LinkarFunctions.UpdateOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.Update(credentialOptions, filename, records, updateOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: UpdatePartial
			Update one or more attributes of one or more file records, with MV input and output format.
			
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords. Use <StringFunctions.ComposeUpdateBuffer> (Linkar.Strings library) function to compose this string.
			dictionaries - (string) List of dictionaries to write, separated by space. In MV output format is mandatory. You may use the format LKFLDx where x is the attribute number.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.

		Returns:
			string
		
			The results of the operation.
			
		Remarks:
		Inside the records argument, the recordIds and the modified records always must be specified. But the originalRecords not always.
		When <UpdateOptions> argument is specified and the <UpdateOptions.OptimisticLockControl> property is set to true, a copy of the record must be provided before the modification (originalRecords argument)
		to use the Optimistic Lock technique. This copy can be obtained from a previous <Read> operation. The database, before executing the modification, 
		reads the record and compares it with the copy in originalRecords, if they are equal the modified record is executed.
		But if they are not equal, it means that the record has been modified by other user and its modification will not be saved.
		The record will have to be read, modified and saved again.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions.Linkar.Functions import LinkarFunctions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyUpdatePartial():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.UpdatePartial(credentials, "LK.CUSTOMERS", 
									"2" + LinkarFunctions.ASCII_Chars.FS_str +				# RecordId
									"CUSTOMER 2" + LinkarFunctions.ASCII_Chars.FS_chr +		# Record
									""														# OriginalRecord
								, "NAME")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def UpdatePartial(credentialOptions, filename, records, dictionaries, updateOptions=LinkarFunctions.UpdateOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.UpdatePartial(credentialOptions, filename, records, dictionaries, updateOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: New
			Creates one or several records of a file, with MV input and output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) The file name where the records are going to be created.
			records - (string) Buffer of records to write. Inside this string are the recordIds, and the records. Use <StringFunctions.ComposeNewBuffer> function to compose this string.
			newOptions - (<NewOptions>) Object with write options for the new record(s), including recordIdType, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Remarks:
			Inside the records argument, the records always must be specified.
			But the recordIds only must be specified when <NewOptions> argument is NULL, or when the <RecordIdType> argument of the <NewOptions> constructor is NULL.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions.Linkar.Functions import LinkarFunctions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyNew():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.New(credentials, "LK.CUSTOMERS", 
									"2" + LinkarFunctions.ASCII_Chars.FS_chr +		# RecordId
									"CUSTOMER 2þADDRESS 2þ444"						# Record
								)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def New(credentialOptions, filename, records, newOptions=LinkarFunctions.NewOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.New(credentialOptions, filename, records, newOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Delete
			Deletes one or several records in file, with MV input and output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) The file name where the records are going to be created.
			records - (string) Buffer of records to be deleted. Use StringFunctions.ComposeDeleteBuffer (Linkar.Strings library) function to compose this string.
			deleteOptions - (<DeleteOptions>) Object with options to manage how records are deleted, including optimisticLockControl, recoverRecordIdType.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.

		Returns:
			string
			
			The results of the operation.
			
		Remarks:
			Inside the records argument, the recordIds always must be specified. But the originalRecords not always.
			When <deleteOptions> argument is specified and the <DeleteOptions.OptimisticLockControl> property is set to true,
			a copy of the record must be provided before the deletion to use the Optimistic Lock technique.
			This copy can be obtained from a previous <Read> operation. The database, before executing the deletion, 
			reads the record and compares it with the copy in originalRecords, if they are equal the record is deleted.
			But if they are not equal, it means that the record has been modified by other user and the record will not be deleted.
			The record will have to be read, and deleted again.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions.Linkar.Functions import LinkarFunctions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyDelete():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Delete(credentials, "LK.CUSTOMERS", 
									"2" + LinkarFunctions.ASCII_Chars.FS_chr +		# RecordId
									""												# OriginalRecord
								)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Delete(credentialOptions, filename, records, deleteOptions=LinkarFunctions.DeleteOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.Delete(credentialOptions, filename, records, deleteOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Select
			Executes a Query in the Database, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) Name of file on which the operation is performed. For example LK.ORDERS
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			sortClause - (string) Statement fragment specifies the selection order. If there is a selection rule, Linkar will execute a SSELECT, otherwise Linkar will execute a SELECT. For example BY CUSTOMER
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM. You may use the format LKFLDx where x is the attribute number.
			preSelectClause - (string) An optional command that executes before the main Select
			selectOptions - (<SelectOptions>) Object with options to manage how records are selected, including calculated, dictionaries, conversion, formatSpec, originalRecords, onlyItemId, pagination, regPage, numPage.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
			
		Remarks:
			In the preSelectClause argument these operations can be carried out before executing the Select statement:
			
				- Previously call to a saved list with the GET.LIST command to use it in the Main Select input
				- Make a previous Select to use the result as the Main Select input, with the SELECT or SSELECT commands.In this case the entire sentence must be indicated in the PreselectClause. For example:SSELECT LK.ORDERS WITH CUSTOMER = '1'
				- Exploit a Main File index to use the result as a Main Select input, with the SELECTINDEX command. The syntax for all the databases is SELECTINDEX index.name.value. For example SELECTINDEX ITEM,"101691"

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MySelect():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Select(credentials, "LK.CUSTOMERS")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Select(credentialOptions, filename, selectClause="", sortClause="", dictClause="", preSelectClause="", selectOptions=LinkarFunctions.SelectOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.Select(credentialOptions, filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions, LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Subroutine
			Executes a subroutine, with MV input and output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			subroutineName - (string) Name of BASIC subroutine to execute.
			argsNumber - (number) Number of arguments.
			arguments - (string) The subroutine arguments list. Each argument is a substring separated with the ASCII char DC4 (20).
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions.Linkar.Functions import LinkarFunctions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MySubroutine():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Subroutine(credentials, "SUB.DEMOLINKAR", 3,	# 3 arguments
									"0" + LinkarFunctions.ASCII_Chars.DC4_chr +				# Argument 1 (input): sleep seconds
									"qwerty" + LinkarFunctions.ASCII_Chars.DC4_chr +		# Argument 2 (input): text to convert to uppercase
									""														# Argument 3 (output): text converted to uppercase
								)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Subroutine(credentialOptions, subroutineName, argsNumber, args, customVars="", receiveTimeout=0):
		return DirectFunctions.Subroutine(credentialOptions, subroutineName, argsNumber, args, LinkarFunctions.DATAFORMAT_TYPE.MV, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Conversion
			Returns the result of executing ICONV() or OCONV() functions from a expression list in the Database, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			conversionType - (<CONVERSION_TYPE>) Indicates the conversion type, input or output: INPUT=ICONV(); OUTPUT=OCONV()
			expression - (string) The data or expression to convert. May include MV marks (value delimiters), in which case the conversion will execute in each value obeying the original MV mark.
			code - (string) The conversion code. Must obey the Database conversions specifications.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyConversion():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Conversion(credentials, CONVERSION_TYPE.INPUT,"31-12-2017þ01-01-2018","D2-")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Conversion(credentialOptions, conversionType, expression, code, customVars="", receiveTimeout=0):
		return DirectFunctions.Conversion(credentialOptions, conversionType, expression, code, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout )
	"""
		Function: Format
			Returns the result of executing the FMT function in a expressions list in the Database, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			expression - (string) The data or expression to format. If multiple values are present, the operation will be performed individually on all values in the expression.
			formatSpec - (string) Specified format.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyFormat():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Format(credentials, "1þ2","R#10")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Format(credentialOptions, expression, formatSpec, customVars="", receiveTimeout=0):
		return DirectFunctions.Format(credentialOptions, expression, formatSpec, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Dictionaries
			Returns all the dictionaries of a file, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) File name.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyDictionaries():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Dictionaries(credentials, "LK.CUSTOMERS")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Dictionaries(credentialOptions, filename, customVars="", receiveTimeout=0):
		return DirectFunctions.Dictionaries(credentialOptions, filename, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: Execute
			Allows the execution of any command from the Database, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			statement - (string) The command you want to execute in the Database.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyExecute():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.Execute(credentials, "WHO")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def Execute(credentialOptions, statement, customVars="", receiveTimeout=0):
		return DirectFunctions.Execute(credentialOptions, statement, LinkarFunctions.DATAFORMAT_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: GetVersion
			Allows getting the server version, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			This function returns the following information:
			
				LKMVCOMPONENTSVERSION - MV Components version.
				LKSERVERVERSION - Linkar SERVER version.
				LKCLIENTVERSION - Used client library version.
				DATABASE - Database.
				OS - Operating system.
				DATEZERO - Date zero base in YYYYMMDD format.
				DATEOUTPUTCONVERSION - Output conversion for date used by Linkar Schemas.
				TIMEOUTPUTCONVERSION - Output conversion for time used by Linkar Schemas.
				MVDATETIMESEPARATOR - DateTime used separator used by Linkar Schemas, for instance 18325,23000.
				MVBOOLTRUE - Database used char for the Boolean true value used by Linkar Schemas.
				MVBOOLFALSE - Database used char for the Boolean false value used by Linkar Schemas.
				OUTPUTBOOLTRUE - Used char for the Boolean true value out of the database used by Linkar Schemas.
				OUTPUTBOOLFALSE - Used char for the Boolean false value out of the database used by Linkar Schemas.
				MVDECIMALSEPARATOR - Decimal separator in the database. May be point, comma or none when the database does not store decimal numbers. Used by Linkar Schemas.
				OTHERLANGUAGES - Languages list separated by commas.
				TABLEROWSEPARATOR - It is the decimal char that you use to separate the rows in the output table format. By default 11.
				TABLECOLSEPARATOR - It is the decimal char that you use to separate the columns in the output table format. By default 9.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyGetVersion():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.GetVersion(credentials)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def GetVersion(credentialOptions, receiveTimeout=0):
		return DirectFunctions.GetVersion(credentialOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, receiveTimeout)

	"""
		Function: LkSchemas
			Returns a list of all the Schemas defined in Linkar Schemas, or the EntryPoint account data files, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			lkSchemasOptions - (<LkSchemasOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			TABLE output format uses the defined control characters in <EntryPoints Parameters: http://kosday.com/Manuals/en_web_linkar/lk_schemas_ep_parameters.html> Table Row Separator and Column Row Separator.
			
			By default:
			
				TAB - char (9) for columns.
				VT - char (11) for rows.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyLkSchemas():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.LkSchemas(credentials)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def LkSchemas(credentialOptions, lkSchemasOptions=LinkarFunctions.LkSchemasOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.LkSchemas(credentialOptions, lkSchemasOptions, LinkarFunctions.DATAFORMATSCH_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: LkProperties
			Returns the Schema properties list defined in Linkar Schemas or the file dictionaries, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) File name to LkProperties.
			lkPropertiesOptions - (<LkPropertiesOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			TABLE output format uses the defined control characters in <EntryPoints Parameters: http://kosday.com/Manuals/en_web_linkar/lk_schemas_ep_parameters.html> Table Row Separator and Column Row Separator.
			
			By default:
			
				TAB - char (9) for columns.
				VT - char (11) for rows.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyLkProperties():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.LkProperties(credentials, "LK.CUSTOMERS")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def LkProperties(credentialOptions, filename, lkPropertiesOptions=LinkarFunctions.LkPropertiesOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.LkProperties(credentialOptions, filename, lkPropertiesOptions, LinkarFunctions.DATAFORMATSCH_TYPE.MV, customVars, receiveTimeout)

	"""
		Function: ResetCommonBlocks
			Resets the COMMON variables with the 100 most used files, with MV output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_MV.Linkar.Functions.Direct.MV.Functions import Functions as DirectFunctions
			def MyResetCommonBlocks():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.ResetCommonBlocks(credentials)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
				
				return result
		---
	"""
	@staticmethod
	def ResetCommonBlocks(credentialOptions, receiveTimeout=0):
		return DirectFunctions.ResetCommonBlocks(credentialOptions, LinkarFunctions.DATAFORMAT_TYPE.MV, receiveTimeout)
