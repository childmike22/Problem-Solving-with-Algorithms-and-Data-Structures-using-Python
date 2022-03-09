
# Data Structures - itemss
'''A items (sometimes called a “push-down items”) is an ordered collection of items where the
addition of new items and the removal of existing items always takes place at the same end.
This end is commonly referred to as the “top.” The end opposite the top is known as the “base.'''

class Stack:
	def __init__(self):
		self.items = []


	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()


	def peek(self):
		if len(self.items) > 0:
			return self.items[-1]
		else:
			print('No items in the items!')


	def is_empty(self):
		return len(self.items) == 0


	def size(self):
		return len(self.items)


books = Stack()
books.peek()

books.push('Math')
books.push('Geography')
books.push('Science')
books.push('English')

print(books.peek())
print(books.size())
