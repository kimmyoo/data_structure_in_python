from stack import Stack

def reverse_file(file_name):
	'''reverse lines in a txt file'''
	s = Stack()
	
	original = open (file_name)
	for line in original:
		s.push(line.strip('\n'))
	original.close()

	output = open(file_name, 'w')
	while not s.is_empty():
		output.write(s.pop() + '\n')
	output.close()
	print ("lines are reversed")
	
# code to test reverse_file(file_name)
file_name = "stack_text"
reverse_file(file_name)


# however, this is the not the best solution to reverse a list
# two pointers pointing to the start and end then swap 
def reverse_list(input_list):
	"""
	input type: list
	return type: list
	"""
	s = Stack()
	recpt = []
	for ele in input_list:
		s.push(ele)
		ele = None

	for ele in input_list:
		print (ele)

	for n in range (0, len(input_list)):
		recpt.append(s.pop())
	return recpt

#input_list = range (10), 
# CANNOT USE ASSIGNMENT ON THE LIST CREATED BY RANGE

input_list = [None] * 10
for x in range (10):
	input_list[x] = x
print ('original list: ',input_list)
print ('reversed: ', reverse_list (input_list))


def is_matched (exprs):
	"""
	return True if delimiters are matched
	input type: string or list
	return type: bool
	"""
	s = Stack()
	lefts = '({['
	rights = ')}]'
	
	for char in exprs:
		if char in lefts:
			s.push(char)
		elif char in rights:
			if s.is_empty():
				return False
			# .index() returns the index associated with a particular element
			if rights.index(char) != lefts.index(s.pop()):
				return False
				
	return s.is_empty()

input_exprs = '[(5+2) - 3] *9'
expression = ['(', ')']
print (is_matched(input_exprs))
print (is_matched(expression))
	
