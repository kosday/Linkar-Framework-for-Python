"""
	enum: DATAFORMATSCH_TYPE
	Specify the output formats of LkSchemas operations.
	Used only by LkSchemas functions.
	There are 4 possible options: MV, XML, JSON and TABLE.
		
	Defined constants of DATAFORMATSCH_TYPE:
	--- Code
		MV - 0x01
		XML - 0x02
		JSON - 0x03
		TABLE - 0x04
	---
"""
class DATAFORMATSCH_TYPE:
	MV = 0x01
	XML = 0x02
	JSON = 0x03
	TABLE = 0x04