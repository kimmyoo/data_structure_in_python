class Empty (Exception):
	pass

class Stack:
	def __init__ (self):
		self.data = []
	
	def is_empty(self):
		return len(self.data) == 0
	
	def len(self):
		return len(self.data)
	
	def push(self, element):
		self.data.append(element)
	
	def peek_top(self):
		if self.is_empty():
			raise Empty ("stack is empty!")
		return self.data[-1]
	
	def pop(self):
		if self.is_empty():
			raise Empty ("stack is empty")
		return self.data.pop()
		


