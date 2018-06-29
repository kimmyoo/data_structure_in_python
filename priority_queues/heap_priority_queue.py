from priority_queue_base import PriorityQueueBase

class Empty (Exception):
	pass

class HeapPriorityQueue(PriorityQueueBase):
#-------------- nonpublic behaviors
    def _parent(self, j):
        return (j-1)//2  # floor division
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    # recursive method to bubble up the item with a smaller key
    def _upheap(self, j):
        parent = self._parent(j)
        # j > 0 make sure the recursion stops at the root
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) # recursion at the positon of parent
    
    # recursive way to sink down an item with larger key
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left # remember the index
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right  # remember the index
            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child) # swapped the content
                self._downheap(small_child) # small_child is just an index
    
#--------------- public behaviors 
    def __init__(self):
        self._data = [] # a plain list
    
    def __len__(self):
        return len(self._data)
        
    def add(self, key, value):
        self._data.append(self._Item(key, value)) # added to the last 
        self._upheap(len(self._data) -1) # recursive uphead starts here
    
    def min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty!")
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty!")
        self._swap(0, len(self._data)-1) # swap root and the last item
        item = self._data.pop() # pop the last item
        self._downheap(0)
        return (item._key, item._value)

#some tests
import os
file_name = "key_value_pairs.txt"

hp_prty_qu = HeapPriorityQueue()
hp_prty_qu.add(5, 'love')
print (hp_prty_qu.min())
hp_prty_qu.add(1, 'think')
print (hp_prty_qu.min())
hp_prty_qu.add(0, 'run')
print (hp_prty_qu.min())
hp_prty_qu.remove_min()
print (hp_prty_qu.min())
print (len(hp_prty_qu))


# open a file and read key, value pairs into a dictionary 
# and add pairs to priority queues
container = {}
try:
    with open (file_name) as file_object:
        for line in file_object:
            (key, value) = line.split(",")
            container[int(key)] = value.strip()
except FileNotFoundError:
    print ("not found")
else:
    for key in container:
        hp_prty_qu.add(key, container[key])

hp_prty_qu.remove_min()
print(hp_prty_qu.min())
print (len(hp_prty_qu))
