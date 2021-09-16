from Linkar_Functions.Linkar.Functions import LinkarFunctions
from ..ENVELOPE_FORMAT import ENVELOPE_FORMAT
from Linkar import Linkar

linkar = Linkar.Linkar()

"""
"""
class DirectCommands:

    """
		Function: SendCommand
			Allows a variety of direct operations using standard templates (XML, JSON).
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			command - (string) Content of the operation you want to send.
			commandFormat - (string) Indicates in what format you are doing the operation: XML or JSON.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
		string
		
		The results of the operation.
    """
    @staticmethod
    def SendCommand(credentialOptions, command, commandFormat, receiveTimeout = 0):
        customVars = ""  # It's inside the command template
        options = "" # It's inside the command template
        opArgs = customVars + LinkarFunctions.ASCII_Chars.US_str + options + LinkarFunctions.ASCII_Chars.US_str + command
        if commandFormat == ENVELOPE_FORMAT.JSON:
            opCode = LinkarFunctions.OPERATION_CODE.COMMAND_JSON
        else:
            opCode = LinkarFunctions.OPERATION_CODE.COMMAND_XML
        inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
        outputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
        
        result = linkar.LkExecuteDirectOperation(credentialOptions, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)
        return result

    """
		Function: SendJsonCommand
			Allows a variety of direct operations using standard JSON templates.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			command - (string) Content of the operation you want to send.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely. 
		
		Returns:
		string
		
		The results of the operation.
		
		Example:
		---Code
            from Linkar.Linkar import CredentialOptions
            from Linkar_Commands.Linkar.Commands.Direct.DirectCommands import DirectCommands
            def MySendCommand():
                try:
                    credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
                    result = DirectCommands.SendJsonCommand(credentials, 
                                "{" +
                                "	\"NAME\" : \"READ\"," +
                                "	\"COMMAND\" :" +
                                "	{" + 
                                "		\"CALCULATED\" : \"True\" ," +
                                "		\"OUTPUT_FORMAT\" : \"JSON_DICT\" ," +
                                "		\"FILE_NAME\" : \"LK.CUSTOMERS\" ," +
                                "		\"RECORDS\" : [" +
                                "			{ \"LKITEMID\" : \"2\" }" +
                                "		]" +
                                "	}" +
                                "}")
                except Exception as ex:
                    result = ""
                    print("ERROR: " + str(ex))
                
                return result
		---
	    """
    @staticmethod
    def SendJsonCommand(credentialOptions, command, receiveTimeout = 0):
        return DirectCommands.SendCommand(credentialOptions, command, ENVELOPE_FORMAT.JSON, receiveTimeout )


    """
		Function: SendXmlCommand
			Allows a variety of direct operations using standard XML templates.
		
		Arguments:
			"credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			"command - (string) Content of the operation you want to send.
			"receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
		string
		
		The results of the operation.
		
		Example:
		---Code
        	from Linkar.Linkar import CredentialOptions
        	from Linkar_Commands.Linkar.Commands.Direct.DirectCommands import DirectCommands
        	def MySendCommand():
                try:
                    credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
                    result = DirectCommands.SendXmlCommand(credentials,
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
    @staticmethod
    def SendXmlCommand(credentialOptions, command, receiveTimeout = 0):
        return DirectCommands.SendCommand(credentialOptions, command, ENVELOPE_FORMAT.XML, receiveTimeout )
