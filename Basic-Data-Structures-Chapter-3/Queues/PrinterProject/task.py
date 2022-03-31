import random


class Task:
	def __init__(self, created_time):
		self.created_time = created_time
		self.num_pages = random.randint(1, 20)


	def get_stamp(self):
		return self.created_time


	def get_pages(self):
		return self.num_pages


	def waiting_times(self, current_time):
		return current_time - self.created_time
