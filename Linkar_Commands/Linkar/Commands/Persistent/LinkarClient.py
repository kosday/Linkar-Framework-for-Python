from Linkar_Functions.Linkar.Functions import LinkarFunctions
from ..ENVELOPE_FORMAT import ENVELOPE_FORMAT
from Linkar import Linkar

linkar = Linkar.Linkar()

"""
	Class: LinkarClient
		These functions perform synchronous persistent (establishing permanent session) operations with any kind of output format type.
		Property: SessionId
		string
		
		SessionID of the connection.
		Property: ReceiveTimeout
		number
		
		Maximum time in seconds that the client will wait for a response from the server.
		Default = 0 to wait indefinitely.
		When the receiveTimeout argument is omitted in any operation, the value set here will be applied.
"""
class LinkarClient:

	"""
		Constructor: __init__
			Initializes a new instance of the LinkarClient class.
			
		Arguments:
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely. When the receiveTimeout argument is omitted in any operation, the value set here will be applied.
	"""
	def __init__(self, receiveTimeout=0):
		self.SessionId = ""
		if receiveTimeout:
			self.ReceiveTimeout = receiveTimeout
		self.ConnectionInfo = None

	"""
		Function: Login
			Starts the communication with a server allowing making use of the rest of functions until the Logout method is executed or the connection with the server gets lost.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Remarks:
			Login is actually a "virtual" operation which creates a new Client Session ID. No DBMS login is performed unless Linkar SERVER determines new Database Sessions are required - these operations are not related.
	"""
	def Login(self, credentialOptions, customVars="", receiveTimeout=0):
		if self.ConnectionInfo is None:
			options = ""
			loginArgs = customVars if customVars else "" + LinkarFunctions.ASCII_Chars.US_chr + options
			byteOpCode = LinkarFunctions.OPERATION_CODE.LOGIN
			byteInputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
			byteOutputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
			receiveTimeout = receiveTimeout if receiveTimeout else 0
			
			if receiveTimeout <= 0 and self.ReceiveTimeout > 0:
				receiveTimeout = self.ReceiveTimeout

			connectionInfo = Linkar.ConnectionInfo("", "", "", credentialOptions)
			loginResult = linkar.LkExecutePersistentOperation(connectionInfo, byteOpCode, loginArgs, byteInputFormat, byteOutputFormat, receiveTimeout)
			if loginResult is not None or len(loginResult) > 0:
				self.ConnectionInfo = connectionInfo
				self.SessionId = connectionInfo.SessionId
			else:
				self.ConnectionInfo = None
				self.SessionId = None

	"""
		Function: Logout
			Closes the communication with the server, that previously has been opened with a Login function.
		
		Arguments:
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.</param>
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.</param>
		Remarks:
			Logout is actually a "virtual" operation which disposes the current Client Session ID. No DBMS logout is performed.
	"""
	def Logout(self, customVars="", receiveTimeout=0):
		logoutArgs = customVars if customVars else ""
		byteOpCode = LinkarFunctions.OPERATION_CODE.LOGOUT
		byteInputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		byteOutputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		receiveTimeout = receiveTimeout if receiveTimeout else 0
		if receiveTimeout <= 0 and self.ReceiveTimeout > 0:
			receiveTimeout = self.ReceiveTimeout

		loginResult = linkar.LkExecutePersistentOperation(self.ConnectionInfo, byteOpCode, logoutArgs, byteInputFormat, byteOutputFormat, receiveTimeout)
		if loginResult is not None or len(loginResult) > 0:
			self.ConnectionInfo = None

	"""
		Function: SendCommand
			Allows a variety of persistent operations using standard templates (XML, JSON).
		
		Arguments:
			command - (string) Content of the operation you want to send.
			commandFormat - (<ENVELOPE_FORMAT>) Indicates in what format you are doing the operation: XML or JSON.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.

		Returns:
			string
			
			The results of the operation.
	"""
	def SendCommand(self, command, commandFormat, receiveTimeout=0):
		customVars = ""  # It's inside the command template
		options = "" # It's inside the command template
		opArgs = customVars + LinkarFunctions.ASCII_Chars.US_str + options + LinkarFunctions.ASCII_Chars.US_str + command
		if commandFormat == ENVELOPE_FORMAT.JSON:
		 	opCode = LinkarFunctions.OPERATION_CODE.COMMAND_JSON
		else:
		 	opCode = LinkarFunctions.OPERATION_CODE.COMMAND_XML
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		outputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: SendJsonCommand
			Allows a variety of persistent operations using standard JSON templates.
		
		Arguments:
			command - (string) Content of the operation you want to send.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
			
		Example:
		---Code
			from Linkar_Commands.Linkar.Commands.Persistent.LinkarClient import LinkarClient
			from Linkar.Linkar import CredentialOptions
			def MySendCommand():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					client = LinkarClient()
					client.Login(credentials)
					result = client.SendJsonCommand(
									"{"
									"	\"NAME\" : \"READ\","
									"	\"COMMAND\" :" 
									"	{"
									"		\"CALCULATED\" : \"True\" ,"
									"		\"OUTPUT_FORMAT\" : \"JSON_DICT\" ,"
									"		\"FILE_NAME\" : \"LK.CUSTOMERS\" ,"
									"		\"RECORDS\" : ["
									"			{ \"LKITEMID\" : \"2\" }"
									"		]"
									"	}"
									"}")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
					
				return result
		---
	"""
	def SendJsonCommand(self, command, receiveTimeout = 0):
		return self.SendCommand(command, ENVELOPE_FORMAT.JSON, receiveTimeout)

	"""
		Function: SendXmlCommand
			Allows a variety of persistent operations using standard XML templates.
		
		Arguments:
			command - (string) Content of the operation you want to send.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
			
		Example:
		---Code
			from Linkar_Commands.Linkar.Commands.Persistent.LinkarClient import LinkarClient
			from Linkar.Linkar import CredentialOptions
			def MySendCommand():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					client = LinkarClient()
					client.Login(credentials)
					result = client.SendXmlCommand(
									"&lt;COMMAND NAME=\"READ\"&gt;"
									"   &lt;CALCULATED&gt;True&lt;/CALCULATED&gt;"
									"   &lt;OUTPUT_FORMAT&gt;XML_DICT&lt;/OUTPUT_FORMAT&gt;"
									"   &lt;FILE_NAME&gt;LK.CUSTOMERS&lt;/FILE_NAME&gt;"
									"   &lt;RECORDS&gt;"
									"       &lt;RECORD&gt;"
									"           &lt;LKITEMID&gt;2&lt;/LKITEMID&gt;"
									"       &lt;/RECORD&gt;"
									"   &lt;/RECORDS&gt;"
									"&lt;/COMMAND&gt;")				
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))
					
				return result
		---
	"""
	def SendXmlCommand(self, command, receiveTimeout = 0):
		return self.SendCommand(command, ENVELOPE_FORMAT.XML, receiveTimeout)
