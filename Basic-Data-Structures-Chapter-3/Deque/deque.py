# "The deque abstract data type is defined by the following structure and operations. A deque is
#structured, as described above, as an ordered collection of items where items are added and
#removed from either end, either front or rear."

class Deque:
	def __init__(self, lst):
		self.lst = lst


	def __str__(self):
		return f"{self.lst}"


	def is_empty(self):
		return len(self.lst) == 0


	def add_rear(self, item):
		self.lst.insert(0, item)


	def add_front(self, item):
		self.lst.append(item)


	def size(self):
		return len(self.lst)


	def remove_rear(self):
		return self.lst.pop(0)


	def remove_front(self):
		return self.lst.pop()


d = Deque([])
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front("True")
d.size()
d.is_empty()
d.add_rear(8.4)
d.remove_rear()
d.remove_front()

# print(d)
