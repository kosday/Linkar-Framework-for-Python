from Linkar_Functions.Linkar.Functions.OPERATION_CODE  import OPERATION_CODE
import os, platform, ctypes

encoding = 'latin1'
class LinkarCLib:
	def __init__(self):
		
		os_arch = platform.architecture()[0]
		
		# Invalid Platform. Don't go ahead.
		if os_arch != "64bit" and os_arch != "32bit":
			return
		
		# Valid Platform.
		lib_path = os.path.dirname(os.path.realpath(__file__))
		if os.name == "nt":
			lib_path += "/DLL/x" + os_arch.replace("bit", "") + "/Linkar.dll"
			self.encoding = "cp1252"
		else:
			lib_path += "/linux.so/x" + os_arch.replace("bit", "") + "/libLinkar.so"
			self.encoding = "iso-8859-1"

		self.lib_linkar = ctypes.cdll.LoadLibrary(lib_path)
		#self.encoding = encoding

linkar = LinkarCLib()

"""
	Class: CredentialOptions
		Contains the necessary information to connect to the Database.

		Property: Host (string)
			Address or hostname where Linkar Server is listening.

		Property: EntryPoint (string)
			The EntryPoint Name defined in Linkar Server.

		Property: Port (number)
			Port number where the EntryPoint keeps listening.

		Property: Username (string)
			Linkar Server username.

		Property: Password (string)
			Password of the Linkar Server user.

		Property: Language (string)
			Used to make the database routines know in which language they must answer. The Error messages coming from the Database are in English by default, but you can customize

		Property: FreeText (string)
			Free text that will appear in the Linkar MANAGER to identify in an easy way who is making the petition. For example if the call is made from a ERP, here we can write "MyERP".

		Property: PluginId (string)
			Internal ID for plugin to enable its use in Linkar Server. Used by Plugin developers.
"""
class CredentialOptions:

	"""
		Constructor: __init__
			Initializes a new instance of CredentialOptions class.

		Arguments:
			host - Address or hostname where Linkar Server is listening.
			entrypoint - The EntryPoint Name defined in Linkar Server.
			port - Port number where the EntryPoint keeps listening.
			username - Linkar Server username.
			password - Password of the Linkar Server user.
			language - Used to make the database routines know in which language they must answer. The Error messages coming from the Database are in English by default, but you can customize.
			freeText - Free text that will appear in the Linkar MANAGER to identify in an easy way who is making the petition. For example if the call is made from a ERP, here we can write "MyERP".
			pluginId - Internal ID for plugin to enable its use in Linkar Server. Used by Plugin developers.
	"""
	def __init__(self, host, entrypoint, port, username, password, language="", freetext="", pluginId=""):
		self.Host = host
		self.EntryPoint = entrypoint
		self.Port = port
		self.Username = username
		self.Password = password
		self.Language = language
		self.FreeText = freetext
		self.PluginId = pluginId
	

	def toString(self):
		return '\u001C'.join([
			self.Host,
			self.EntryPoint,
			str(self.Port),
			self.Username,
			self.Password,
			self.Language,
			self.FreeText,
			self.PluginId
		])


"""
	Class: ConnectionInfo
		Contains the necessary information to stablished a permanent session with LinkarSERVER. Used by Login operation and Permanent operations.
"""
class ConnectionInfo:
	"""
		Constructor: __init__
			Initializes a new instance of the CredentialOptions class

		Arguments:
			sessionId - A unique Identifier for the stablished session in LinkarSERVER. This value is set after Login operation.
			lkConnectionId - Internal LinkarSERVER ID to keep the session. This value is set after Login operation.
			publicKey - The public key used to encrypt transmission data between LinkarCLIENT and LinkarSERVER. This value is set after Login operation.
			crdOptions - The <CredentialOptions> object with the necessary information to connect to the LinkarSERVER.
	"""
	def __init__(self, sessionId, lkConnectionId, publicKey, crdOptions):
		self.SessionId = sessionId
		self.LkConnectionId = lkConnectionId
		self.PublicKey = publicKey
		self.CredentialOptions = crdOptions
		self.ReceiveTimeout = 0

	def fromString(self, string):
		seperator = '\u001C'
		creds = string.split(seperator)
		self.CredentialOptions = CredentialOptions(
			creds[0], creds[1], int(creds[2]),
			creds[3], creds[4], creds[5], creds[6]
		)
		self.SessionId = creds[8]
		self.LkConnectionId = creds[9]
		self.PublicKey = creds[10]
		self.ReceiveTimeout = creds[11]

	def toString(self):
		return '\u001C'.join([
			self.CredentialOptions.toString(),
			self.SessionId,
			self.LkConnectionId,
			self.PublicKey,
			str(self.ReceiveTimeout)
		])

"""
	Class: Linkar
		Class with two static functions to perform Direct and Persistent operation with Linkar Server
"""
class Linkar:

	def __init__(self):
		pass

	""" Linkar functions. """
	def LkFreeMemory(self, lkString):
		linkar.lib_linkar.LkFreeMemory(lkString)

	""" Utils (Not from C) """
	def LkAllocateBuffer(self, input_buffer):
		return ctypes.create_string_buffer(input_buffer)

	""" Linkar """
	"""
		Function:	LkExecuteDirectOperation
			Execute "direct operations". These operations don't stablish a permanent session. Once the operations is finished, the session is closed.

		Arguments:
			credentialOptions - (<CredentialOptions>) The credentials for access to LinkarSERVER.
			operationCode - (<OPERATION_CODE>) Code of the operation to be performed.
			operationArgs - (string) Specific arguments of every operation.
			inputDataFormat - (number <DATAFORMAT_TYPE>, <DATAFORMATCRU_TYPE> or <DATAFORMATSCH_TYPE>) Format of the input data.
			outputDataFormat - (number <DATAFORMAT_TYPE>, <DATAFORMATCRU_TYPE> or <DATAFORMATSCH_TYPE>) Format of the output data.
			receiveTimeout - (number) Maximum time in seconds to wait the response from LinkarSERVER. A value less or equal to 0, wait for response indefinitely.

		Returns:
			Complex string with the result of the operation.
	"""
	def LkExecuteDirectOperation(self, credentialOptions, operationCode, operationArgs, inputDataFormat, outputDataFormat, receiveTimeout):
		error = ""
		pError = ctypes.c_char_p(error.encode(linkar.encoding))
		
		linkar.lib_linkar.LkExecuteDirectOperation.argtypes = [
			ctypes.POINTER(ctypes.c_char_p),		# error (char**)
			ctypes.c_char_p,						# credentialOptions (char*)	
			ctypes.c_uint8,							# operationCode (uint8_t)
			ctypes.c_char_p,						# operationArgs (char*)
			ctypes.c_uint8,							# inputDataFormat (uint8_t)
			ctypes.c_uint8,							# outputDataFormat (uint8_t)
			ctypes.c_uint32							# receiveTimeout (uint32_t)
		]
		linkar.lib_linkar.LkExecuteDirectOperation.restype = ctypes.c_void_p
		co = credentialOptions.toString()
		ret_cxx_value = linkar.lib_linkar.LkExecuteDirectOperation(
			pError,
			ctypes.c_char_p(co.encode(linkar.encoding)),
			operationCode,
			ctypes.c_char_p(operationArgs.encode(linkar.encoding)),
			inputDataFormat,
			outputDataFormat,
			receiveTimeout)
		
		if ret_cxx_value is not None:
			ret_value = ctypes.cast(ret_cxx_value, ctypes.c_char_p).value
			self.LkFreeMemory(ctypes.cast(ret_cxx_value, ctypes.c_char_p))
			return str(ret_value, linkar.encoding)
		else:
			msgError = pError.value.decode(linkar.encoding)
			self.LkFreeMemory(ctypes.cast(pError, ctypes.c_char_p))
			raise Exception(msgError)
		
	"""
		Function:	LkExecutePersistentOperation
			Execute "persistent operations". These operations required that a session will be stablished previously with Login operation.
		
		Arguments:
			connectionInfo - (<ConnectionInfo>) Contains the data necessary to access an established LinkarSERVER session.
			operationCode - (<OPERATION_CODE>) Code of the operation to be performed.
			operationArgs - (string) Specific arguments of every operation.
			inputDataFormat - (number <DATAFORMAT_TYPE>, <DATAFORMATCRU_TYPE> or <DATAFORMATSCH_TYPE>) Format of the input data.
			outputDataFormat - (number <DATAFORMAT_TYPE>, <DATAFORMATCRU_TYPE> or <DATAFORMATSCH_TYPE>) Format of the output data.
			receiveTimeout - (number) Maximum time in seconds to wait the response from LinkarSERVER. A value less or equal to 0, wait for response indefinitely.
			
		Returns:
			Complex string with the result of the operation. 
	"""
	def LkExecutePersistentOperation(self, connectionInfo, operationCode, operationArgs, inputDataFormat, outputDataFormat, receiveTimeout):
		error = ""
		pError = ctypes.c_char_p(error.encode(linkar.encoding))

		strConnInfo = connectionInfo.toString()
		pConnInfo = ctypes.c_char_p(strConnInfo.encode(linkar.encoding))

		linkar.lib_linkar.LkExecutePersistentOperation.argtypes = [
			ctypes.POINTER(ctypes.c_char_p),		# error (char**)
			ctypes.POINTER(ctypes.c_char_p),		# connectionInfo (char**)
			ctypes.c_uint8,							# operationCode (uint8_t)
			ctypes.c_char_p,						# operationArgs (char*)
			ctypes.c_uint8,							# inputDataFormat (uint8_t)
			ctypes.c_uint8,							# outputDataFormat (uint8_t)
			ctypes.c_uint32							# receiveTimeout (uint32_t)
		]

		linkar.lib_linkar.LkExecutePersistentOperation.restype = ctypes.c_void_p
		ret_cxx_value = linkar.lib_linkar.LkExecutePersistentOperation(
			pError,
			pConnInfo,
			operationCode,
			ctypes.c_char_p(operationArgs.encode(linkar.encoding)),
			inputDataFormat,
			outputDataFormat,
			receiveTimeout)

		if ret_cxx_value is not None:
			if operationCode == OPERATION_CODE.LOGIN:
				strConnInfo = pConnInfo.value.decode(linkar.encoding)
				self.LkFreeMemory(ctypes.cast(pConnInfo, ctypes.c_char_p))
				connectionInfo.fromString(strConnInfo)

			ret_value = ctypes.cast(ret_cxx_value, ctypes.c_char_p).value
			self.LkFreeMemory(ctypes.cast(ret_cxx_value, ctypes.c_char_p))
			return str(ret_value, linkar.encoding)
		else:
			msgError = pError.value.decode(linkar.encoding)
			self.LkFreeMemory(ctypes.cast(pError, ctypes.c_char_p))
			raise Exception(msgError)
