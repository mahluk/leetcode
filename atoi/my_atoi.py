#!/usr/local/bin/python3.7

def isValid(ch,first_ch):
    
    ascii_val = ord(ch)
    
    if ascii_val not in range(49,58):
        if first_ch and (ascii_val == 43 or ascii_val == 45):
            return True
        return False
        
    return True
        
    
def myAtoi(str):
	max_int = pow(2,31) - 1
	min_int = -pow(2,31)
    
	str = str.lstrip(' ')
	negative = False
	result_str = ""

	if isValid(str[0],True):

		if str[0] == '-':
			negative = True
			str = str[1:]
		elif str[0] == "+":
			str = str[1:]

	for c in str:
		if isValid(c,False):
			result_str += c
		else:
			break

	result = 0

	if result_str == "":
		return result

	for i,c in enumerate(result_str[::-1]):
		result += int(c) * pow(10,i)

	if result >= max_int:
		return max_int
	elif result <= min_int:
		return min_int

	return result if not negative else -result

	return 0

if __name__ == '__main__':
	pass

