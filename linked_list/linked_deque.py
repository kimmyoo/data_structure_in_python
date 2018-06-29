from dbly_linked_list import DoublyLinkedList
class Empty(Exception):
    pass

#implmentation of LinkedDeque class is inherited from DoublyLinkedList
class LinkedDeque(DoublyLinkedList):
    def get_head(self):
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self.header.next.element
    
    def get_tail(self):
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self.trailer.prev.element
    
    def insert_first(self, ele):
        new_node = self._insert_between(ele, self.header, 
                                        self.header.next)
        return new_node
    
    def insert_last(self, ele):
        new_node = self.insert_between(ele, self.tailer.prev, 
                                        self.trailer)
        return new_node
        
    def delete_head(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._del_node(self.header.next)
    
    def delete_tail(self):
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._del_node(self.trailer.prev)
        
    
        
    



# some tests on the DoublyLinkedList class in dbly_linked_list.py
d_list = DoublyLinkedList()
inserted_node = d_list._insert_between('new node', d_list.header, 
                d_list.trailer)
print (d_list.header.next.element)
d_list._del_node(inserted_node)
print (d_list.__len__())

# some tests on the LinkedDeque class
l_deque = LinkedDeque()
for n in range(10):
    l_deque.insert_first(n)

print(l_deque.get_head())
print(l_deque.get_tail())

for n in range(10):
    deleted_node = l_deque.delete_tail()
    print(deleted_node)
    

