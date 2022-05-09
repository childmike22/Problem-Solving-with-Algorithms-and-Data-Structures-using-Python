# create a linked list
class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None


	def __str__(self):
		return f"{self.data}"


	def get_data(self):
		return self.data


	def get_next(self):
		return self.next


	def set_data(self, new_data):
		self.data = new_data


	def set_next(self, new_next):
		self.next = new_next


temp = Node(93)
print(temp.get_data())


'''As we suggested above, the unordered list will be built from a collection of nodes, each linked
to the next by explicit references. As long as we know where to find the first node (containing
the first item), each item after that can be found by successively following the next links. With
this in mind, the UnorderedList class must maintain a reference to the first node. The following
code shows the constructor. Note that each list object will maintain a single reference to the
head of the list.'''

class UnorderedList:
	def __init__(self):
		self.head = None


	def __str__(self):
		res = ''

		ptr = self.head
		while ptr:
			res += f'{ptr} -- > '
			ptr = ptr.get_next()

		res += 'NONE'

		return res


	def is_empty(self):
		return self.head == None


	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp


	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()

		return count


	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()
			
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found:
			if current.get_data() == item:
				found=True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())






mylist = UnorderedList()
# mylist.head = 8

print(mylist.is_empty())

mylist.add(23)
mylist.add(77)
mylist.add(17)

print(mylist.head)


print(mylist.is_empty())

print(mylist.size())
print(mylist.search(3))
print(mylist.search(77))

mylist.remove(77)

print(mylist)
