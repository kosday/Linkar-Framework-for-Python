import os, platform, ctypes
from cffi import FFI

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
		else:
			lib_path += "/linux.so/x" + os_arch.replace("bit", "") + "/libLinkar.so"

		self.lib_linkar = ctypes.cdll.LoadLibrary(lib_path)
		self.encoding = encoding


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
		__init__() -- constructor
			initializes a new instance of CredentialOptions class.

		Arguments --
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
		__init__() -- constructor
			Initializes a new instance of the CredentialOptions class

		Arguments:
			sessionId - A unique Identifier for the stablished session in LinkarSERVER. This value is set after Login operation.
			lkConnectionId - Internal LinkarSERVER ID to keep the session. This value is set after Login operation.
			publicKey - The public key used to encrypt transmission data between LinkarCLIENT and LinkarSERVER. This value is set after Login operation.
			crdOptions - The CredentialOptions object with the necessary information to connect to the LinkarSERVER.
	"""
	def __init__(self, sessionId, lkConnectionId, publicKey, crdOptions):
		self.SessionId = sessionId
		self.LkConnectionId = lkConnectionId
		self.PublicKey = publicKey
		self.CredentialOptions = crdOptions
		self.ReceiveTimeout = 0

	def fromString(self, string):
		seperator = '\u001C';
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
			self.ReceiveTimeout
		])


"""
	Class: Linkar
		Class with two static functions to perform Direct and Persistent operation with Linkar Server
"""
class Linkar:

	def __init__(self):
		pass


	""" Linkar functins. """
	def LkFreeMemory(self, lkString):
		linkar.lib_linkar.LkFreeMemory(lkString)


	""" Utils (Not from C) """
	def LkAllocateBuffer(self, input_buffer):
		return ctypes.create_string_buffer(input_buffer)
		# return ctypes.c_char_p(input_buffer)


	def LkCloneAndFree(self, ret_cxx_value, free):
		
		if ret_cxx_value is None:
			size = 0
			ret_cxx_value = ctypes.c_bool
		else:
			size = ctypes.sizeof(ret_cxx_value)
		buff = ctypes.resize(ret_cxx_value, size)
		# var buff = ref.reinterpretUntilZeros(ret_cxx_value, 1)
		# output_buffer = self.LkAllocateBuffer(str.encode(buff))
		
		if free:
			self.LkFreeMemory(ret_cxx_value)
		return output_buffer


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
		pointer = ctypes.c_wchar_p()
		pOperationArgs = self.LkAllocateBuffer(operationArgs.encode(encoding=encoding))
		
		try:
			linkar.lib_linkar.LkExecuteDirectOperation.argtypes = [
				ctypes.POINTER(ctypes.c_wchar_p),
				ctypes.c_wchar_p,
				ctypes.c_uint8,
				ctypes.c_char_p,
				ctypes.c_uint8,
				ctypes.c_uint8,
				ctypes.c_uint32
			]
			linkar.lib_linkar.LkExecuteDirectOperation.restype = ctypes.c_wchar_p

			co = credentialOptions.toString()
			ret_cxx_value = linkar.lib_linkar.LkExecuteDirectOperation(
				ctypes.byref(pointer),
				co,
				operationCode,
				pOperationArgs,
				inputDataFormat,
				outputDataFormat,
				receiveTimeout
			)
			return ret_cxx_value
		except Exception as e:
			return ">>> " + str(e)
		
		# if ret_cxx_value is not None:
		# 	return self.LkCloneAndFree(ret_cxx_value, True)
		# else:
		# 	errPointer = ctypes.byref(pointer)
		# 	print(errPointer)
			# raise self.LkCloneAndFree(errPointer, True).toString(linkar.encoding)
			# raise Exception("\n\nDirect Operation return value is \"None\".\n")



	def LkExecutePersistentOperation(self, connectionInfo, operationCode, operationArgs, inputDataFormat, outputDataFormat, receiveTimeout):
		pointer = ctypes.create_string_buffer(1)
		pOperationArgs = self.LkAllocateBuffer(str.encode(operationArgs)) # pass str as bytes type.
		pointerConnInfo = ctypes.create_string_buffer(connectionInfo.toString())
		ret_cxx_value = linkar.lib_linkar.LkExecutePersistentOperation(pointer, pointerConnInfo, operationCode, pOperationArgs, inputDataFormat, outputDataFormat, receiveTimeout)

		if ret_cxx_value is not None:
			print("Success result. Parsing Values.")
		else:
			# errPointer = ctypes.byref(pointer)
			# raise self.LkCloneAndFree(errPointer, True).toString(linkar.encoding)
			raise Exception("\n\nPersistent Operation return value is \"None\".\n")