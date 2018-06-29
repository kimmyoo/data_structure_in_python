class Empty(Exception):
    pass

class CircLinkedQueue:
    class Node:
        __slot__ = 'element', 'next'
        def __init__(self, ele, nxt):
            self.element = ele
            self.next = nxt
    
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def len(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_first(self):
        if self.is_empty():
            raise Empty ("empty queue!")
        head = self.tail.next
        return head.element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("empty queue!")
        head = self.tail.next
        rtn = head.element
        if self.size == 1:
            self.tail = None
        else: 
            self.tail.next = head.next
        self.size -= 1
        return rtn
    
    def enqueue(self, element):
        new_node = self.Node (element, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next


sample_list = ['abc', 'acb', 'bca', 'bac']
q = CircLinkedQueue()

for n in range (4):
    q.enqueue(girl_list[n])

for n in range (4):
    head = q.tail.next
    print (head.element)
    q.rotate()

for n in range (4):
    q.dequeue()

