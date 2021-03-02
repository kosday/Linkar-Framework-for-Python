from . import DBMV_Mark

"""
	Class: MvOperations
		This class contains the basic functions to work with multivalue strings. These functions are locally executed.
"""
class MvOperations:
	"""
		Function: LkDCount
			Counts the delimited substrings inside a string.
			
		Arguments:
			str - (string) Source string of delimited fields.
			delimiter - (string) The separator character(s) used to delimit fields in the string.
		
		Returns:
			number
			
			The number of occurrences found.
			
		Example:
		---Code
		int result = MvOperations.LkCount("CUSTOMER UPDATE 2þADDRESS 2þ444", "þ");		---
	"""

	@staticmethod
	def LkDCount(input_string, delimiter):
		if input_string is None or len(input_string) == 0:
			return False
		elif delimiter is None or len(delimiter) == 0:
			return len(input_string)
		else:
			# parts = input_string.split(delimiter, -1)
			# return len(parts)
			pass