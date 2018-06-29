from priority_queue_base import PriorityQueueBase
from pos_linked_list import PositionalLinkedList

class Empty (Exception):
	pass

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalLinkedList() # always remember the "()"!!
    
    def __len__(self):
        return len(self._data)
    
    # add method keeps the list sorted and minimum key is always at the
    # first position of the positional list
    def add(self, key, value):
        new = self._Item(key, value)
        walk = self._data.last()
        # here the order of the condition matters!
        # walk is not None will ensure the adding of first element 
        # skips while loop! otherwise the condition tests new < walk.element
        # first and the interpreter will report None type has no element attribute
        while walk is not None and new < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)
        else:
            self._data.add_after(walk, new)
    
    def min(self):
        if self.is_empty():
            raise Empty("priority queue is empty!")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise Empty("priority queue is empty!")
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)

# some tests
priority_list = SortedPriorityQueue()
priority_list.add(5, 'yall')
priority_list.add(9, 'yo~')
priority_list.add(1, 'wow')
print(priority_list.min())
priority_list.remove_min()
print(priority_list.min())
# not suppose to access to private attributes but just for tests
for item in priority_list._data:
    print (item._key, item._value)
            
