from stack import Stack
	
s = Stack()
s.push(5)
s.push(6)
print (s.peek_top())
print (s.pop())
print (s.peek_top())
s.push('dog')
s.push (10)
print (s.len())
while (s.is_empty() == False):
	print (s.pop())
print (s.len())



marks = '$bcde.edcb$'

for i in range (0, len(marks)//2):
	s.push(marks[i])
	
print (s.data)

if len(marks)%2 == 0:
	middle = len(marks)//2
else:
	middle = len(marks)//2 +1 
	
for i in range (middle, len(marks)):
	if marks[i] == s.peek_top():
		s.pop()
if s.len() != 0:
	print ("no matching")
else:
	print ("matching")
