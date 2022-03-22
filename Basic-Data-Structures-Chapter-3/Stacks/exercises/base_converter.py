"""In your study of computer science, you have probably been exposed in one way or another to
the idea of a binary number. Binary representation is important in computer science since all
values stored within a computer exist as a string of binary digits, a string of 0s and 1s. Without
the ability to convert back and forth between common representations and binary numbers, we
would need to interact with computers in very awkward ways.
Integer values are common data items. They are used in computer programs and computation
all the time. We learn about them in math class and of course represent them using the decimal
number system, or base 10. The decimal number 23310 and its corresponding binary equivalent
111010012 are interpreted respectively as 2 * 102 + 3 * 101 + 3 * 100
and 1 * 2
7 + 1 * 2
6 + 1 *
2
5 + 0 * 2
4 + 1 * 2
3 + 0 * 2
2 + 0 * 2
1 + 1 * 2

"""

def divide_by_two(num):
	lst = []
	while num > 0:
		rem = num % 2
		lst.append(rem)
		num = num // 2
	# convert to a string

	str_result = ''
	while len(lst) > 0:
		str_result = str_result + str(lst.pop())
	return str_result


print(divide_by_two(25))



def baseConverter(num, base):
	lst = []
	while num > 0:
		rem = num % base
		lst.append(rem)
		num = num // base
	return lst

print(baseConverter(25,16))
print(baseConverter(25,2))
print(baseConverter(25,8))
