"""
	enum: DATAFORMATSCHPROP_TYPE
	Indicates the format of the data returned by LkProperties function: MV, XML, JSON,JSON_DICT, JSON_SCH, XML_DICT, XML_SCH or TABLE
	
	Defined constants of DATAFORMATSCHPROP_TYPE:
	--- Code
		MV - 0x01
		XML - 0x02
		JSON - 0x03
		TABLE - 0x04
		XML_DICT - 0x05
		XML_SCH - 0x06
		JSON_DICT - 0x07
		JSON_SCH - 0x08
	---
"""
class DATAFORMATSCHPROP_TYPE:
	MV = 0x01
	XML = 0x02
	JSON = 0x03
	TABLE = 0x04
	XML_DICT = 0x05
	XML_SCH = 0x06
	JSON_DICT = 0x07
	JSON_SCH = 0x08