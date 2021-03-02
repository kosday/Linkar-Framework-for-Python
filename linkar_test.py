from Linkar.Linkar import LinkarCLib, CredentialOptions, ConnectionInfo, Linkar
from LinkarFunctions.OperationCode import OPERATIONCODE
from LinkarFunctions.OperationArguments import OperationArguments
from LinkarFunctions.ReadOptions import ReadOptions
from LinkarFunctions.DATAFORMAT_TYPE import DATAFORMAT_TYPE
from LinkarFunctions.DATAFORMATCRU_TYPE import DATAFORMATCRU_TYPE
from LinkarFunctions.SelectOptions import SelectOptions
from ctypes import *

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

		receiveTimeout = 0
		opCode = OPERATIONCODE.LOGIN
		inputFormat = DATAFORMAT_TYPE.MV
		outputFormat = DATAFORMATCRU_TYPE.MV
		filename = 'LK.ORDERS'
		selectClause = "1"
		sortClause = ""
		dictClause = ""
		preSelectClause = ""
		customVars = ""
		opArgs = OperationArguments.GetSelectArgs(filename, selectClause, sortClause, dictClause, preSelectClause, SelectOptions(), customVars)
		
		RS_str = "\u001E";
		US_str = "\u001F";
		AM_str = "\u00FE";
		# buff =  US_str + "0" + AM_str + AM_str + "0" + AM_str + "0" + AM_str + "0" + US_str + "LK.CUSTOMERS" + AM_str + "1" + RS_str + "2" + AM_str;
		# buff = "0þþ0þ0þ0LK.CUSTOMERSþ12þ"
		buff = ""
		r = linkar.LkExecuteDirectOperation(cred_opt, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)
		print("************* Result:")
		print(r)



	Read()
	# a = py_object('abc')
	# b = pointer(a)

	# pointer = POINTER(c_char_p) # memory location with type.
	# print(dir(pointer))
	# print(pointer._objects)
	# print('pointer: ', addressof(pointer._objects))

	# p = create_string_buffer(str.encode(""))
	# print(byref(p))
	# print(p)

	# m = memoryview(b'abcefg') # only memory location.
	
	# cred_opt = client.LkCreateCredentialOptions(
	# 	'linkardemo.ddns.net', 		# host
	# 	'DEMOLINKAR', 				# entryPoint
	# 	21301, 						# entryPoint Port
	# 	'gaurav', 					# username
	# 	'nxy5umpn3wpi2f1ijf78pb', 	# password
	# 	'', 						# lang
	# 	'dummy text' 				# dummy text
	# )

	print("\n\n\n\n")