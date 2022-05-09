from deque import Deque

test = Deque([5,6])


# easy way (using a list method)
def palindrome_checker(a_string):
	return list(a_string) == list(a_string)[::-1]


# try with non-palindromes
print(palindrome_checker('mike'))

# try with palindromes
print(palindrome_checker('racecar')) 
print(palindrome_checker('wow'))


# dequeue method
# remove items from the front / rear of the queue (either they match and we are left with 0 or 1 characters left - depending on if it's odd or even), or it's not a palindrome
def palindrome_checker_deque(a_string):
	is_equal = True
	deque = Deque([])
	for ch in a_string:
		deque.add_front(ch)

	while deque.size() > 1:
		if deque.remove_front() != deque.remove_rear():
			is_equal = False
			break

	return is_equal




# check with palindromes
print(palindrome_checker_deque('radar'))
print(palindrome_checker_deque('racecar'))


# check with non-palindromes
print(palindrome_checker_deque('classroom'))
print(palindrome_checker_deque('rule'))
