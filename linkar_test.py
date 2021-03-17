from Linkar.Linkar import LinkarCLib, CredentialOptions, ConnectionInfo, Linkar
from LinkarFunctions.OPERATION_CODE import OPERATIONCODE
from LinkarFunctions.OperationArguments import OperationArguments
from LinkarFunctions.ReadOptions import ReadOptions
from LinkarFunctions.DATAFORMAT_TYPE import DATAFORMAT_TYPE
from LinkarFunctions.DATAFORMATCRU_TYPE import DATAFORMATCRU_TYPE
from LinkarFunctions.SelectOptions import SelectOptions
from ctypes import *
from LinkarFunctionsDirect.DirectFunctions import DirectFunctions


if __name__ == "__main__":
	print("\n")
	
	client = LinkarCLib()
	cred_opt = CredentialOptions(
		'linkardemo.ddns.net', 		# host
		'DEMOLINKAR', 				# entryPoint
		21301, 						# entryPoint Port
		'gaurav', 					# username
		'nxy5umpn3wpi2f1ijf78pb', 	# password
		'', 						# lang
		'dummy_text'
	)


	def Read():
		linkar = Linkar()

		RS_str = "\u001E"
		US_str = "\u001F"
		AM_str = "\u00FE"
		VM_str = "\u00FD"

		receiveTimeout = 0
		opCode = OPERATIONCODE.SELECT
		inputFormat = DATAFORMAT_TYPE.MV
		outputFormat = DATAFORMATCRU_TYPE.MV
		filename = 'LK.ORDERS'
		selectClause = ""
		sortClause = "BY ID"
		dictClause = ""
		preSelectClause = ""
		customVars = ""
		
		# Select Input Data
		selectInputData = AM_str.join([
			filename,
			selectClause,
			sortClause,
			dictClause,
			preSelectClause
		])
		

		# prepare select Options
		onlyRecordId = False
		pagination = True
		regPage = 10
		numPage = 1
		calculated = False
		conversion = False
		formatSpec = False
		originalRecords = False
		selectOptions = SelectOptions(onlyRecordId, pagination, regPage, numPage, calculated, conversion, formatSpec, originalRecords)

		# Operation Argumens
		opArgs = OperationArguments.GetSelectArgs(filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions, customVars)

		# Execute Direct Function
		print("\n\n*************")
		r = linkar.LkExecuteDirectOperation(cred_opt, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)
		print("*************\n\n")
		print(r)


	Read()

	print("\n\n\n\n")