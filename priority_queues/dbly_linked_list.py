class DoublyLinkedList:
    class Node:
        __slot__ = 'element', 'prev', 'next'
        
        def __init__(self, ele, prv, nxt):
            self.element = ele
            self.prev = prv
            self.next = nxt
        
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

# accessors 
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

# updators 
    #leading underscore means the method is nonpublic
    #insert must indentify the node pairs to which the new node
    #will be in serted
    def _insert_between(self, ele, predecessor, successor):
        new_node = self.Node(ele, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        #successful insertion must return the new node
        return new_node
    
    def _del_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        ele = node.element
        node.prev = node.next = node.element = None
        return ele
