def palindrome_checker(word):
	word = word.strip()
	if len(word) <= 1:
		return True
	else:
		if word[0] == word[-1]:
			return palindrome_checker(word[1:-1])
		else:
			return False





# check palindromes
print(palindrome_checker('kayak'))
print(palindrome_checker('name'))
print(palindrome_checker('live not on evil'))


# check non-palindromes
print(palindrome_checker('california'))
print(palindrome_checker('san francisco'))
