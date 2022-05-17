def add_nums(num_list):
	if len(num_list) == 1:
		return num_list[0]
	else:
		return num_list[0] + add_nums(num_list[1:])


def list_sum(num_list):
	if len(num_list) == 1:
		return num_list[0]
	else:
		return num_list[0] + list_sum(num_list[1:])

  
  
print(list_sum([1,3,5,7,9]))
print(add_nums([33, 22, 1]))
