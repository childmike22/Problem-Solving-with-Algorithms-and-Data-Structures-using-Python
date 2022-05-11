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





class OrderedList:

	def __init__(self):
		self.head = None


	def __str__(self):
		result = ''
		current = self.head

		while current != None:
			result += f" -- > {current.get_data()}"
			current = current.get_next()

		return result


	def add(self, item):
		current = self.head
		previous = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else: 
				previous = current
				current = current.get_next()

		temp = Node(item)
		if previous == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current)
			previous.set_next(temp)






olist = OrderedList()
print(olist)

olist.add(88)
olist.add(67)
olist.add(67)
olist.add(900)
print(olist.head.get_next())
print(olist)
