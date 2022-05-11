# Node class
# properties: item and next
# methods: get_data, set_next, get_next

class Node:
	def __init__(self, item):
		self.data = item
		self.next = None


	def __str__(self):
		return f"(Node: {self.data})"


	def get_data(self):
		return self.data


	def get_next(self):
		return self.next


	def set_next(self, item):
		self.next = item


# n1 = Node(78)
# print(n1.get_next())

# n1.set_next(['hey', 55])
# print(n1.get_next())





# properties: head
# methods = add, size, search, remove

class OrderedList:

	def __init__(self, items):
		self.head = None
		self.items = items

		for item in items:
			self.add(item)


	def __str__(self):
		res_string = ''
		current = self.head

		while current != None:
			res_string += f' --> {current.get_data()}'
			current = current.get_next()

		return res_string


	def size(self):
		count = 0
		current = self.head

		while current != None:
			count += 1
			current = current.get_next()

		return count


	def search(self, num):
		found = False
		curr = self.head

		while curr != None and not found:
			if num == curr.get_data():
				found = True
			else:
				curr = curr.get_next()

		return found


	def add(self, num):
		prev = None
		current = self.head
		stop = False

		while current != None and not stop:
			if current.get_data() > num:
				stop = True
			else:
				prev = current
				current = current.get_next()

		temp = Node(num)

		if prev == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			prev.set_next(temp)
			temp.set_next(current)


trial = OrderedList([45, 90, 32, -13, 987, 3, 21])
trial.add(65)
trial.add(43)
trial.add(1002)
print(trial)
