class Empty (Exception):
	pass

class ArrayQueue:
	'''array-based queue; front index cirlce around (modulo) if reach to the limit of
	array length; if the queue is full, array size doubles automatically
	'''
	DEFAULT_SIZE = 10
	
	def __init__(self):
		self.data = [None] * ArrayQueue.DEFAULT_SIZE
		self.size = 0
		self.front = 0
	
	def get_size (self):
		return self.size
		
	def is_empty(self):
		return self.size == 0
	
	def get_front(self):
		if is_empty():
			raise Empty ('queue is empty!')
		return self.data [self.front]
	
	def dequeue (self):
		'''returns the front element'''
		if self.is_empty():
			raise Empty ('queue is empty')
		# first save the element that needed to be returned
		head = self.data [self.front]
		# for garbage collection 
		self.data[self.front] = None
		# formula to get the next front element's index
		self.front = (self.front + 1) % len(self.data)
		self.size -= 1
		# these two lines were added to adjust the size of the data array 
		# when the num of element is less than 1/4 of the array length
		if 0 < self.size < len (self.data) //4:
			self.resize ( len (self.data)//2 )
		return head
		
	
	def resize (self, alloc):
		# first assign a new reference to the original list to keep track of
		# of the original list
		old_data = self.data
		# allocating 
		self.data = [None] * alloc
		
		# self.front must be remembered
		walk = self.front
		# only consider existing elements
		for n in range (self.size):
			self.data [n] = old_data[walk]
			# looking for the next element to process
			walk = (walk+1) % len(old_data)
		self.front = 0 # adjusting the front index
		
	def enqueue (self, element):
		# 1. check if the queue is full
		# if full, need to resize the array (double)
		# 2. tricky formula to get index for enqueuing
		# formula also works if array is resized
		if self.size == len(self.data):
			self.resize (2*len(self.data))
		avail = (self.front + self.size) % len(self.data)
		self.data[avail] = element
		self.size += 1

