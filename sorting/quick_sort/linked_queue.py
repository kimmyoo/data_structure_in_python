class Empty(Exception):
    pass

class LinkedQueue:
    class Node:
        __slot__ = 'element', 'next'
        def __init__(self, ele, nxt):
            self.element = ele
            self.next = nxt
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self.head.element
    
    def enqueue(self, ele):
        # here None make sure the first node, head's next is none
        # which also satisfies tail's property
        new_node = self.Node(ele, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        # this line ensures that if there's only one element, 
        # head is also the tail
        self.tail = new_node
        # don't forget to update the size
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Empty Queue!")
        rtn = self.head.element
        self.head = self.head.next
        self.size -= 1
        # when the last element is dequeued, 
        # the head refers to None but the tail is still referring to
        # the instance that was pointed by head, so we must refer tail to None
        if self.is_empty():
            self.tail = None
        return rtn
