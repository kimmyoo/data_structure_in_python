from queue import ArrayQueue

q = ArrayQueue()

data_entry = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for data in data_entry:
	q.enqueue(data)
# test to see if the length of the data array is double
print (len(q.data))

data_recptr = []
for n in range (9):
	data_recptr.append(q.dequeue())
print (data_recptr)

# the size of the queue shrinks to less than 1/4, 
# accordingly, the size of the array shrinks to half
print (len(q.data))
