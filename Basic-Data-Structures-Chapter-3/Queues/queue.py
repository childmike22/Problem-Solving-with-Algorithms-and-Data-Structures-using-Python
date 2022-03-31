# Data Structure: Queue

# First in First out (FIFO)

# Examples: line into a movie theatre, spotify playlist, a printer in a lab (connected to 30 computers)

class Queue:
	def __init__(self):
		self.items = []


	def is_empty(self):
		return len(self.items) == 0


	def enqueue(self, item):
		self.items.insert(0, item)


	def dequeue(self):
		return self.items.pop()


	def size(self):
		return len(self.items)



playlist = Queue()
print(playlist.is_empty())

playlist.enqueue('Billie Jean')
playlist.enqueue('Firework')
playlist.enqueue('September')

print(playlist.is_empty())
print(f"Dequeing: {playlist.dequeue()}")
print(playlist.items)

print(playlist.size())


# Game of Hot Potato
def hot_potato(name_list, num):
	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()

	return sim_queue.dequeue()


print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
