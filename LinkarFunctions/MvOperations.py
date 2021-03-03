from . import DBMV_Mark
import sys

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
			parts = input_string.split(delimiter)
			return len(parts)



	"""
		Function: LkCount
			Counts the occurrences of a substring inside a string.
			
		Arguments:
			str - (string) Source string of delimited fields.
			delimiter - (string) The separator character(s) used to delimit fields in the string.
		Returns:
			number
			
			The number of occurrences found.
		Example:
		---Code
		int result = MvOperations.LkDCount("CUSTOMER UPDATE 2þADDRESS 2þ444", "þ");
	"""
	@staticmethod
	def LkCount(input_string, delimiter):
		if input_string is None or len(input_string) == 0:
			return False
		elif delimiter is None or len(delimiter) == 0:
			return len(input_string)
		else:
			return MvOperations.LkDCount(input_string, delimiter) - 1


	"""
		Function: LkExtract
			Extracts a field, value or subvalue from a dynamic array.
			
		Arguments:
			str - (string) The source string from which data is extracted.
			field - (number) The position of the attribute to extract.
			value - (number) The multivalue position to extract.
			subvalue - (number) The subvalue position to extract.
		Returns:
			string
			
			A new string with the extracted value.
		Example:
		---Code
		string result = MvOperations.LkExtract("CUSTOMER UPDATE 2þADDRESS 2þ444", 1);
		---
	"""
	@staticmethod
	def LkExtract(input_string, field, value=0, subvalue=0):
		aux = ""
		if field > 0:
			parts = input_string.split(DBMV_Mark.AM)
			if field <= len(parts):
				input_string = aux = parts[field-1]

		if value > 0:
			parts = input_string.split(DBMV_Mark.VM)
			if value <= len(parts):
				input_string = aux = parts[value-1]

		if subvalue > 0:
			parts = input_string.split(DBMV_Mark.SM)
			if subvalue <= len(parts):
				aux = parts[subvalue-1]

		return aux



	"""
		Function: LkChange
			Replaces the occurrences of a substring inside a string, by other substring.
			
		Arguments:
			str - (string) The string on which the value is going to change.
			strOld - (string) The value to change. 
			strNew - (string) The new value.
			occurrence - (number) The number of times it will change.
			start - (number) The position from which you are going to start changing values.
		Returns:
			string
			
			A new string with replaced text.
		Example:
		---Code
		string result = MvOperations.LkChange("CUSTOMER UPDATE 2þADDRESS 2þ444", "UPDATE", "MYTEXT", 1, 1);
		---
	"""
	@staticmethod
	def LkChange(input_string, strOld, strNew, occurrence=0, start=0):
		if len(input_string) > 0:
			if not start or start < 1:
				start = 1
			if not occurrence or occurrence < 1:
				occurrence = 1
			
			index = input_string.find(strOld)
			if index >= 0:
				subindex = 0
				nxt = True
				count = 0

				while nxt:
					subindex = input_string.find(strOld, subindex)
					count += 1
					if subindex == -1 or count >= start:
						nxt = False
					else:
						subindex = subindex + length(strOld)

				if subindex >= 0:
					initstr = input_string[0: int(subindex)]
					endstr = input_string[int(subindex)]
					maxocc = len(endstr.split(strOld))
					if occurrence and occurrence > 0:
						for x in range(occurrence):
							if x > maxocc:
								break
							endstr = endstr.replace(strOld, strNew)
					else:
						endstr = endstr.replace(strOld, strNew)

					return initstr + endstr
				else:
					return input_string
			else:
				return input_string
		else:
			return input_string


	"""
		Function: LkReplace
			Replaces a field, value or subvalue from a dynamic array, returning the result.
			
		Arguments:
			str - (string) The string on which you are going to replace a value.
			newVal - (string) New value that will be replaced in the indicated string.
			field - (number) The position of the attribute where you want to replace.
			value - (number) The multivalue position where you want to replace.
			subvalue - (number) The subvalue position where you want to replace.
		
		Returns
			string
			
			A new string with the replaced value.
		Example:
		---Code
		string result = MvOperations.LkReplace("CUSTOMER UPDATE 2þADDRESS 2þ444", "MYTEXT", 1);
		---
	"""
	@staticmethod
	def LkReplace(input_string, newVal, field, value=0, subvalue=0):
		result = ""
		input_string_len = len(input_string)
		i = 0
	
		field -= 1
		while field > 0 and input_string_len > 0:
			if input_string[i] == DBMV_Mark.AM:
				field -= 1
			i += 1
			input_string_len -= 1
		
		if field > 0:
			createdstr = "";
			cstr = DBMV_Mark.AM;
			for index in range(field):
				createdstr += cstr
			input_string += createdstr
			i += field
		
		value -= 1
		while value > 0 and input_string_len > 0:
			if input_string[i] == DBMV_Mark.AM:
				break

			if input_string[i] == DBMV_Mark.VM:
				value -= 1

			i += 1
			input_string_len -= 1

		if value > 0:
			createdstr = ""
			cstr = DBMV_Mark.VM
			for index in range(value):
				createdstr += cstr
			input_string += createdstr
			i += value

		subvalue -= 1
		while subvalue > 0 and input_string_len > 0:
			if input_string[i] == DBMV_Mark.VM or input_string[i] == DBMV_Mark.AM:
				break

			if input_string[i] == DBMV_Mark.SM:
				subvalue -= 1

			i += 1
			input_string_len -= 1

		if subvalue > 0:
			createdstr = ""
			cstr = DBMV_Mark.SM
			for index in range(subvalue):
				createdstr += cstr
			input_string += createdstr
			i += subvalue


		if i >= len(input_string):
			result = input_string + newVal
		else:
			nextAM = input_string.find(DBMV_Mark.AM, i)
			if nextAM == -1:
				nextAM = sys.maxsize

			nextVM = input_string.find(DBMV_Mark.VM, i)
			if nextVM == -1:
				nextVM = sys.maxsize

			nextSM = input_string.find(DBMV_Mark.SM, i)
			if nextSM == -1:
				nextSM = sys.maxsize

			j = min(nextAM, min(nextVM, nextSM))
			if j == sys.maxsize:
				j = len(input_string)

			part1 = input_string[0, i]
			part2 = input_string[j]
			result = part1 + newVal + part2

		return result