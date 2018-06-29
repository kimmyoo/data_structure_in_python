from priority_queue_base import PriorityQueueBase
from pos_linked_list import PositionalLinkedList

class Empty (Exception):
	pass

class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalLinkedList() # always remember the "()"!!
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.add_last(self._Item(key, value))
    
    def _find_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty!")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small
    
    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

# some tests
priority_list = UnsortedPriorityQueue()
priority_list.add(5, 'yall')
priority_list.add(9, 'yo~')
priority_list.add(1, 'wow')
print(priority_list.min())
priority_list.remove_min()
print(priority_list.min())
            
