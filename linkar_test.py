from sys import api_version
from platform import win32_edition

from Linkar.Linkar import CredentialOptions
from Linkar_Functions.Linkar.Functions import LinkarFunctions
from Linkar_Strings.Linkar.Strings.StringFunctions import StringFunctions

from Linkar_Functions_Direct.Linkar.Functions.Direct.DirectFunctions import DirectFunctions
from Linkar_Functions_Persistent.Linkar.Functions.Persistent.LinkarClient import LinkarClient

from Linkar_LkData.Linkar.LkData.LkData import LkData
from Linkar_LkData.Linkar.LkData.LkItem import LkItem
from Linkar_LkData.Linkar.LkData.LkDataCRUD import LkDataCRUD
from Linkar_LkData.Linkar.LkData.LkDataSubroutine import LkDataSubroutine
from Linkar_LkData.Linkar.LkData.LkDataExecute import LkDataExecute
from Linkar_LkData.Linkar.LkData.LkDataFormat import LkDataFormat
from Linkar_LkData.Linkar.LkData.LkDataConversion import LkDataConversion
from Linkar_LkData.Linkar.LkData.LkDataSchProp import LkDataSchProp

if __name__ == "__main__":
	print("\n")
	
	credentialOpt = CredentialOptions(
		'192.168.100.101', 		# host
		'QMEP1', 				# entryPoint
		11301, 					# entryPoint Port
		'admin', 				# username
		'admin', 				# password
		'', 					# lang
		'python_test'			# free text
	)

	filename = "LK.CUSTOMERS"
	outputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
	outputFormatCRU = LinkarFunctions.DATAFORMATCRU_TYPE.MV
	outputformatSCH = LinkarFunctions.DATAFORMATSCH_TYPE.TABLE
	inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
	customVars = ""
	receiveTimeout = 10
	lkDataCRUD = LkDataCRUD("")

	def TestNew(withLogin = False):
		print("\nNEW. Create two news records with IDs \"TEST_1\" and \"TEST_2\"")
		readAfter = True
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		recordIdType = LinkarFunctions.RecordIdType()
		newOpt =  LinkarFunctions.NewOptions(recordIdType, readAfter, calculated, conversion, formatSpec, originalRecords)
		
		rec1 = ""
		rec1 = LinkarFunctions.MvOperations.LkReplace(rec1, "CUSTOMER_TEST1", 1)
		rec1 = LinkarFunctions.MvOperations.LkReplace(rec1, "ADDRESS_TEST1", 2)
		rec1 = LinkarFunctions.MvOperations.LkReplace(rec1, "111111111", 3)
		rec2 = "CUSTOMER_TEST2" + LinkarFunctions.DBMV_Mark.AM_str + "ADDRESS_TEST2" + LinkarFunctions.DBMV_Mark.AM_str + "222222222"
		records = StringFunctions.ComposeNewBuffer([ "TEST_1", "TEST_2" ], [ rec1, rec2])
		if withLogin:
			result = linkarClt.New(filename, records, newOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.New(credentialOpt, filename, records, newOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nNEW. Create two news records with IDs \"TEST_3\" and \"TEST_2\" using LkData")
		global lkDataCRUD
		lkDataCRUD.LkRecords.LstDictsId = [ "ID" ]
		lkDataCRUD.LkRecords.LstDicts = ["NAME", "ADDR", "PHONE"]

		rec3 = LkItem("TEST_3")
		lkDataCRUD.LkRecords.push(rec3)
		rec3.set("CUSTOMER_TEST3", 1) # attribute 1 (NAME dictionary)
		rec3.set("ADDRESS_TEST3", "ADDR")
		rec3.set("333333333", "PHONE")		

		rec4 = LkItem("TEST_4")
		lkDataCRUD.LkRecords.push(rec4)
		rec4.set("CUSTOMER_TEST4", "NAME")
		rec4.set("ADDRESS_TEST4", "ADDR")
		rec4.set("444444444", "PHONE")		

		records = lkDataCRUD.LkRecords.ComposeNewBuffer()
		if withLogin:
			result = linkarClt.New(filename, records, newOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.New(credentialOpt, filename, records, newOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("LkData:------------------------------------\n")
		print(lkDataCRUD.LkRecords.LstDictsId[0] + "\t", end="")
		for dic in lkDataCRUD.LkRecords.LstDicts:
			print(dic + "\t\t", end="")
		print("")
		for rec in lkDataCRUD.LkRecords:
			print(rec.RecordId, rec.get("NAME"), rec.get(2), rec.get(3), sep="\t")
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestRead(withLogin = False):
		print("\nREAD. Read record Id \"TEST_1\"")
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		readOpt = LinkarFunctions.ReadOptions(calculated, conversion, formatSpec, originalRecords)	
		recordIds = "TEST_1"
		dictionaries = ""
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		if withLogin:
			result = linkarClt.Read(filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Read(credentialOpt, filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("READ. Read recordId TEST_1 and TEST_2")
		recordIds = StringFunctions.ComposeRecordIds(["TEST_1", "TEST_2"])
		if withLogin:
			result = linkarClt.Read(filename, recordIds, dictionaries, readOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Read(credentialOpt, filename, recordIds, dictionaries, readOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nREAD. Read recordId TEST_3 and TEST_4 using LkData")
		global lkDataCRUD
		lkDataCRUD.LkRecords.pushIds([ "TEST_3", "TEST_4" ])
		recordIds = lkDataCRUD.LkRecords.ComposeReadBuffer()
		if withLogin:
			result = linkarClt.Read(filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Read(credentialOpt, filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("LkData:------------------------------------")
		lkDataCRUD = LkDataCRUD(result)
		print(lkDataCRUD.LkRecords.LstDictsId[0] + "\t", end="")
		for dic in lkDataCRUD.LkRecords.LstDicts:
			print(dic + "\t\t", end="")
		print("")
		for rec in lkDataCRUD.LkRecords:
			print(rec.RecordId, rec.get(1), rec.get(2), rec.get(3), sep="\t")

		print("\nlkData.LkRecords[1].get(2) --> " + lkDataCRUD.LkRecords[1].get(2))
		print("lkData.LkRecords.get(\"TEST_4\").get(2) --> " + lkDataCRUD.LkRecords.get("TEST_4").get(2))
		print("lkData.LkRecords.get(\"TEST_4\").get(\"ADDR\") --> " + lkDataCRUD.LkRecords.get("TEST_4").get("ADDR"))
		print("lkData.LkRecords.get(\"TEST_4\").get(\"ADDR\", 1, 1) --> " + lkDataCRUD.LkRecords.get("TEST_4").get("ADDR", 1, 1))
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestUpdate(withLogin = False):
		print("\nUPDATE. Read and Update the record with ID \"TEST_1\"")		
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		readOpt = LinkarFunctions.ReadOptions(calculated, conversion, formatSpec, originalRecords)
		recordIds = "TEST_1"
		dictionaries = ""
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		if withLogin:
			result = linkarClt.Read(filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Read(credentialOpt, filename, recordIds, dictionaries, readOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)

		##orgRec1 = StringFunctions.ExtractRecords(result)[0]
		orgRec1 = ""
		rec1 = LinkarFunctions.MvOperations.LkReplace(orgRec1, "UPDATE_ADDRESS_TEST_1", 2)
		records = StringFunctions.ComposeUpdateBuffer(recordIds, rec1, orgRec1)

		optimisticLockControl = False
		readAfter = True
		originalRecords = False
		updateOpt = LinkarFunctions.UpdateOptions(optimisticLockControl, readAfter, calculated, conversion, formatSpec, originalRecords)
		if withLogin:
			result = linkarClt.Update(filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Update(credentialOpt, filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nUPDATE. Update the records with ID \"TEST_3\" and \"TEST_4\" using LkData")
		print("LkData:------------------------------------\n")
		global lkDataCRUD
		lkDataCRUD.LkRecords[0].set("UPDATE_ADDRESS_TEST_3", 2)
		lkDataCRUD.LkRecords.get("TEST_4").set("UPDATE_ADDRESS_TEST_4", 2)
		records = lkDataCRUD.LkRecords.ComposeUpdateBuffer()
		if withLogin:
			result = linkarClt.Update(filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Update(credentialOpt, filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)

		lkDataCRUD = LkDataCRUD(result)
		print(lkDataCRUD.LkRecords.LstDictsId[0] + "\t", end="")
		for dic in lkDataCRUD.LkRecords.LstDicts:
			print(dic + "\t\t", end="")
		print("")
		for rec in lkDataCRUD.LkRecords:
			print(rec.RecordId, rec.get(1), rec.get(2), rec.get(3), sep="\t")
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestUpdatePartial(withLogin = False):
		print("\nUPDATEPARTIAL. Update only the attibute 2 (ADDR) on the record with ID \"TEST_2\"")
		optimisticLockControl = False
		readAfter = True
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		updateOpt = LinkarFunctions.UpdateOptions(optimisticLockControl, readAfter, calculated, conversion, formatSpec, originalRecords)

		recordId = "TEST_2"
		dictionaries = "ADDR"
		attributeValue = "UPDATE_ADDRESS_TEST_2"
		orgRecord = ""
		records = StringFunctions.ComposeUpdateBuffer(recordId, attributeValue, orgRecord)
		if withLogin:
			result = linkarClt.UpdatePartial(filename, records, dictionaries, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.UpdatePartial(credentialOpt, filename, records, dictionaries, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nUPDATEPARTIAL. Update only the attibute 2 (ADDR) on the record with ID \"TEST_4\"")
		print("LkData:------------------------------------")
		recordId = "TEST_4"
		dictionaries = "ADDR"
		attributeValue = "UPDATE_ADDRESS_TEST_4"
		orgRecord = ""
		records = StringFunctions.ComposeUpdateBuffer(recordId, attributeValue, orgRecord)
		if withLogin:
			result = linkarClt.Update(filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Update(credentialOpt, filename, records, updateOpt, inputFormat, outputFormatCRU, customVars, receiveTimeout)
		lkData = LkDataCRUD(result)
		print(lkData.LkRecords.LstDictsId[0] + "\t", end="")
		for dic in lkData.LkRecords.LstDicts:
			print(dic + "\t\t", end="")
		print("")
		for rec in lkData.LkRecords:
			print(rec.RecordId, rec.get(1), rec.get(2), rec.get(3), sep="\t")
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestDelete(withLogin = False):
		print("\nDELETE. Delete the records with IDs \"TEST_1\" and \"TEST_2\"")
		optimisticLockControl = False
		recoverIdType = LinkarFunctions.RecoverIdType()
		deleteOpt = LinkarFunctions.DeleteOptions(optimisticLockControl, recoverIdType)
		recordIds = StringFunctions.ComposeRecordIds([ "TEST_1", "TEST_2" ])
		originalRecords = ""
		records = StringFunctions.ComposeDeleteBuffer(recordIds, originalRecords)
		if withLogin:
			result = linkarClt.Delete(filename, records, deleteOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Delete(credentialOpt, filename, records, deleteOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nDELETE. Delete the records with IDs \"TEST_1\" and \"TEST_2\" with LkData")
		print("LkData:------------------------------------")
		global lkDataCRUD
		records = lkDataCRUD.LkRecords.ComposeDeleteBuffer()
		if withLogin:
			result = linkarClt.Delete(filename, records, deleteOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Delete(credentialOpt, filename, records, deleteOpt, inputFormat, outputFormat, customVars, receiveTimeout)
		lkDataCRUD = LkDataCRUD(result)
		for rec in lkDataCRUD.LkRecords:
			print(rec.RecordId, "DELETED", sep="\t")
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestSelect(withLogin = False):
		print("\nSELECT. Select all records of the LK.CUSTOMERS file")
		onlyRecordId = False
		pagination = False
		regPage = 10
		numPage = 2
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		selectOpt = LinkarFunctions.SelectOptions(onlyRecordId, pagination, regPage, numPage, calculated, conversion, formatSpec, originalRecords)

		selectClause = ""
		sortClause = "BY ID"
		dictClause = ""
		preselectClause = ""
		if withLogin:
			result = linkarClt.Select(filename, selectClause, sortClause, dictClause, preselectClause, selectOpt, outputFormatCRU, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Select(credentialOpt, filename, selectClause, sortClause, dictClause, preselectClause, selectOpt, outputFormatCRU, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:------------------------------------")
		lkData = LkDataCRUD (result)
		print(lkData.LkRecords.LstDictsId[0] + "\t", end="")
		for dic in lkData.LkRecords.LstDicts:
			print(dic + "\t\t", end="")
		print("")
		for rec in lkData.LkRecords:
			print(rec.RecordId, rec.get(1), rec.get(2), rec.get(3), sep="\t")
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestSubroutine(withLogin = False):
		print("\nSUBROUTINE. Call to SUB.DEMOLIKAR subroutine")
		subroutineName = "SUB.DEMOLINKAR"
		argsNumber = "3"
		args = StringFunctions.ComposeSubroutineArgs(["0", "aaaaaaaaa", ""])
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		if withLogin:
			result = linkarClt.Subroutine(subroutineName, argsNumber, args, inputFormat, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Subroutine(credentialOpt, subroutineName, argsNumber, args, inputFormat, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:------------------------------------")
		lkData = LkDataSubroutine(result)
		i = 1
		for arg in lkData.Arguments:
			print("Arg " + str(i) + ": " + arg)
			i += 1
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestConversion(withLogin = False):
		print("\nCONVERSION")
		expression = StringFunctions.ComposeExpressions(["31-12-2017", "01-01-2018"])
		code = "D2-"
		conversionType = LinkarFunctions.CONVERSION_TYPE.INPUT
		if withLogin:
			result = linkarClt.Conversion(conversionType, expression, code, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Conversion(credentialOpt, conversionType, expression, code, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:------------------------------------")
		lkData = LkDataConversion(result)
		print(" Conversion: " + lkData.Conversion)
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestFormat(withLogin = False):
		print("\nFORMAT")
		expression = "1"
		formatSpec = "R#10"
		if withLogin:
			result = linkarClt.Format(expression, formatSpec, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Format(credentialOpt, expression, formatSpec, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:-----------------------------------")
		lkData = LkDataFormat(result)
		print(" Format: " + lkData.Format)
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestExecute(withLogin = False):
		print("\nEXECUTE")
		statement = "WHO"
		if withLogin:
			result = linkarClt.Execute(statement, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Execute(credentialOpt, statement, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:------------------------------------")
		lkData = LkDataExecute(result)
		print(" Capturing: " + lkData.Capturing)
		print(" Returning: " + lkData.Returning)
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestDictionaries(withLogin = False):
		print("\nDICTIONARIES")
		if withLogin:
			result = linkarClt.Dictionaries(filename, outputFormat, customVars, receiveTimeout)
		else:
			result = DirectFunctions.Dictionaries(credentialOpt, filename, outputFormat, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:------------------------------------")
		lkData = LkDataCRUD(result)
		for rec in lkData.LkRecords:
			print(rec.RecordId + "\t\t" + rec.Record)
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestGetVersion(withLogin = False):
		print("\nGETVERSION")
		if withLogin:
			result = linkarClt.GetVersion(outputFormat, receiveTimeout)
		else:
			result = DirectFunctions.GetVersion(credentialOpt, outputFormat, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		lstTags = StringFunctions.ExtractRecordsDicts(result)
		lstValues = StringFunctions.ExtractRecords(result)[0].split(LinkarFunctions.DBMV_Mark.AM)
		i = 0
		for tag in lstTags:
			print(" " + tag + "\t\t" + lstValues[i])
			i += 1
		print("-------------------------------------------")
		input("Press any key to continue")

	def TestLkSchemas(withLogin = False):
		print("\nLKSCHEMAS")

		print("\nSchemaType: LKSCHEMAS")
		rowHeader = LinkarFunctions.ROWHEADERS_TYPE.MAINLABEL
		rowProperties = True
		onlyVisibles = False
		pagination = False
		regPage = 10
		numPage = 1
		lkSchemasOpt = LinkarFunctions.LkSchemasOptions()
		lkSchemasOpt.LkSchemas(rowHeader, rowProperties, onlyVisibles, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.LkSchemas(lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkSchemas(credentialOpt, lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:-------------------------------------")
		lkData = LkDataSchProp(result)
		print("RowProperties: ")
		for prop in lkData.RowProperties:
			print("\t" + prop)
		print("\nRowHeaders: ")
		for header in lkData.RowHeaders:
			print("\t" + header)
		print("\n-------------------------------------------")

		print("\nSchemaType: SQL MODE")
		lkSchemasOpt.SqlMode(onlyVisibles, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.LkSchemas(lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkSchemas(credentialOpt, lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")
		print("LkData:-------------------------------------")
		lkData = LkDataSchProp(result)
		print("RowProperties: ")
		for prop in lkData.RowProperties:
			print("\t" + prop)
		print("\nRowHeaders: ")
		for header in lkData.RowHeaders:
			print("\t" + header)
		print("\n-------------------------------------------")

		print("\nSchemaType: DICTIONARIES")
		lkSchemasOpt.Dictionaries(rowHeader, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.LkSchemas(lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkSchemas(credentialOpt, lkSchemasOpt, outputformatSCH, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestLkProperties(withLogin = False):
		print("\nLKPROPERTIES")

		print("\nSchemaType: LKSCHEMAS")
		rowHeader = LinkarFunctions.ROWHEADERS_TYPE.MAINLABEL
		rowProperties = False
		onlyVisibles = False
		usePropertyNames = False
		pagination = False
		regPage = 10
		numPage = 1
		lkPropertiesOpt = LinkarFunctions.LkPropertiesOptions()
		lkPropertiesOpt.LkSchemas(rowHeader, rowProperties, onlyVisibles, usePropertyNames, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.LkProperties(filename, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkProperties(credentialOpt, filename, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nSchemaType: SQL MODE")
		lkPropertiesOpt.SqlMode(onlyVisibles, pagination, regPage, numPage)
		filenameSql = "CUSTOMERS"
		if withLogin:
			result = linkarClt.LkProperties(filenameSql, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkProperties(credentialOpt, filenameSql, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nSchemaType: DICTIONARIES")
		lkPropertiesOpt.Dictionaries(rowHeader, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.LkProperties(filename, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		else:
			result = DirectFunctions.LkProperties(credentialOpt, filename, lkPropertiesOpt, outputformatSCH, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestGetTable(withLogin = False):
		print("\nGETTABLE")

		print("\nSchemaType: LKSCHEMAS")
		rowHeader = LinkarFunctions.ROWHEADERS_TYPE.MAINLABEL
		rowProperties = False
		usePropertyNames = False
		repeatValues = False
		applyConversion = False
		applyFormat = False
		calculated = False
		pagination = False
		regPage = 10
		numPage = 1
		tableOpt = LinkarFunctions.TableOptions()
		tableOpt.LkSchemas(rowHeader, rowHeader, rowProperties, usePropertyNames, repeatValues, applyConversion, applyFormat, calculated, pagination, regPage, numPage)
		selectClause = ""
		dictClause = ""
		sortClause = "BY ID"
		if withLogin:
			result = linkarClt.GetTable(filename, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		else:
			result = DirectFunctions.GetTable(credentialOpt, filename, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nSchemaType: SQL MODE")
		onlyVisibles = False
		tableOpt.SqlMode(onlyVisibles, applyConversion, applyFormat, calculated, pagination, regPage, numPage)
		filenameSql = "CUSTOMERS"
		if withLogin:
			result = linkarClt.GetTable(filenameSql, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		else:
			result = DirectFunctions.GetTable(credentialOpt, filenameSql, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nSchemaType: DICTIONARIES")
		tableOpt.Dictionaries(rowHeader, repeatValues, applyConversion, applyFormat, calculated, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.GetTable(filename,  selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		else:
			result = DirectFunctions.GetTable(credentialOpt, filename,  selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		print("\nSchemaType: NONE")
		tableOpt.Nothing(rowHeader, repeatValues, pagination, regPage, numPage)
		if withLogin:
			result = linkarClt.GetTable(filename, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		else:
			result = DirectFunctions.GetTable(credentialOpt, filename, selectClause, dictClause, sortClause, tableOpt, customVars, receiveTimeout)
		print("TABLE result:--------------------------------\n" + result)
		print("-------------------------------------------")

		input("Press any key to continue")

	def TestResetCommonBlocks(withLogin = False):
		if withLogin:
			result = linkarClt.ResetCommonBlocks(outputFormat, receiveTimeout)
		else:
			result = DirectFunctions.ResetCommonBlocks(credentialOpt, outputFormat, receiveTimeout)
		print("Raw result:--------------------------------\n" + result)
		print("-------------------------------------------")

		input("Press any key to continue")

	try:
		print("Test DIRECT Functions\n")
		TestNew()
		TestRead()
		TestUpdate()
		TestUpdatePartial()
		TestDelete()
		TestSelect()
		TestSubroutine()
		TestConversion()
		TestFormat()
		TestExecute()
		TestDictionaries()
		TestGetVersion()
		TestLkSchemas()
		TestLkProperties()
		TestGetTable()
		TestResetCommonBlocks()

		print("Test PERSISTENT Functions (with Login)\n")

		linkarClt = LinkarClient()
		linkarClt.Login(credentialOpt, customVars, receiveTimeout)
		TestNew(True)
		TestRead(True)
		TestUpdate(True)
		TestUpdatePartial(True)
		TestDelete(True)
		TestSelect(True)
		TestSubroutine(True)
		TestConversion(True)
		TestFormat(True)
		TestExecute(True)
		TestDictionaries(True)
		TestGetVersion(True)
		TestLkSchemas(True)
		TestLkProperties(True)
		TestGetTable(True)
		TestResetCommonBlocks(True)
		linkarClt.Logout(customVars, receiveTimeout)

	except Exception as ex:
		print("ERROR: " + str(ex))
		
	print("\n\n\n\n")