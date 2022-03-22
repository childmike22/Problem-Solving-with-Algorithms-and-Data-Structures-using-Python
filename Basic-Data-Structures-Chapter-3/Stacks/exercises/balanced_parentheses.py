# Balanced Parentheses (same symbol)


relationship = {'(': ')'}


string1 = '(()()()())'
string2 = '(((())))'
string3 = '()))'


def balanced_parentheses(string):
	
    result_lst = []

    for s in string:
        if s in relationship.keys():
            result_lst.append(s)
	else:
	    if len(result_lst) == 0:
	        return False
	    else:
		result_lst.pop()
				
				
    if len(result_lst) == 0:
	return True
    else:
	return False


print(balanced_parentheses(string1))
print(balanced_parentheses(string2))
print(balanced_parentheses(string3))
