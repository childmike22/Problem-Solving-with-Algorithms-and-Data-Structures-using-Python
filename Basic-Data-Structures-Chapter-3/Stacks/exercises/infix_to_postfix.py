def infix_to_postfix(input_string):
	values = {
		'*': 3, 
		'/': 3, 
		'+': 2, 
		'-': 2, 
		'(': 1
	}

	op_stack = []
	output_list = []


	input_list = input_string.split()
	print(input_list)


	for x in input_list:
		if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or x in"0123456789":
			output_list.append(x)
		elif x == '(':
			op_stack.append(x)
		elif x == ')':
			top_token = op_stack.pop()
			while top_token != '(':
				output_list.append(top_token)
				top_token = op_stack.pop()

		else:
			while (not len(op_stack) == 0) and (values[op_stack[-1]] >= values[x]):
				output_list.append(op_stack.pop())
			op_stack.append(x)

	while len(op_stack) > 0:
		output_list.append(op_stack.pop())


	return(" ".join(output_list))

print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
