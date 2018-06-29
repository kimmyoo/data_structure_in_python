class Empty (Exception):
    pass

class LinkedStack:
    '''stack structure implemented with singly-linked list'''
# nested Node class_______________________________
    class Node:
        __slot___ = 'element', 'next'
        def __init__(self, ele, nxt):
            self.element = ele
            self.next = nxt
        
# stack constructor and methods__________________________________
    def __init__(self):
        #doc strings also needs to be correctly indented
        '''create an empty stack''' 
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
        
    def len(self):
        return self.size
    
    def get_top(self):
        if self.is_empty():
            raise Empty ("stack is empty!")
        return self.head.element
        
    # be careful about the self in fron tof Node
    def push(self, ele):
        new_node = self.Node(ele, self.head)
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise Empty ('empty stack!')
        rtned = self.head.element
        self.head = self.head.next
        self.size -= 1
        return rtned

#implement some tests here
