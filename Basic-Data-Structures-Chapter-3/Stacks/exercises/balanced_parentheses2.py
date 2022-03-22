symbol_dict = {
	'(': ')', 
	'{':'}', 
	'[': ']'
}



def balanced_parentheses(string):
    opening_list = []
    if len(string) <= 1 or string[0] in symbol_dict.values():
		return False

    for symbol in string:
	if symbol in symbol_dict.keys():
	    opening_list.append(symbol_dict[symbol])
	else: 
	    if symbol != opening_list.pop():
	        return False

    if len(opening_list) == 0:
        return True
    else:
        return False


print(balanced_parentheses('[[]]'))
print(balanced_parentheses('[[]'))
print(balanced_parentheses('(){}'))
print(balanced_parentheses(('{{([][])}()}')))
print(balanced_parentheses('[[]}'))
