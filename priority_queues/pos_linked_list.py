from dbly_linked_list import DoublyLinkedList

class PositionalLinkedList(DoublyLinkedList):
    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node
        
        def element(self):
            return self.node.element
        ## __eq__ is ==
        def __eq__(self, other):
            return type(self) is type(other) and self.node is other.node
        
        def __ne_(self, other):
            return not (self == other)

## utility method of PositionalLinedList class
    def _validate(self, p):
        """return position's node or raise error if invalid
        还原出node"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p.container is not self:
            raise ValueError("p doesn't not belong to this container")
        if p.node.next is None:
            raise ValueError("p is no longer valid")
        return p.node
    
    def _make_position(self, node):
        """return the position instance for a given node, return none 
        if the given node is a sentinel node"""
        # this ensures that if the list is empty, first() will return None
        if node is self.header or node is self.trailer:
            return None
        else:
            #self is the container!
            return self.Position(self, node)
    
## accessors 
    def first(self):
        """returns the first position in the list rather than element
        returns none if the lis is empty"""
        return self._make_position(self.header.next)
    
    def last(self):
        return self._make_position(self.trailer.prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)
        
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
## mutators from parent class DoublyLinkedList
    # it uses super() to refer to the parent class
    def _insert_between(self, e, predecessor, successor):
        """
        add element between existing nodes and return new Position
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self.header, self.header.next)
    
    def add_last(self, e):
        return self._insert_between(e, self.trailer.prev, self.trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original.prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)
    
    def delete(self, p):
        """returns the element in the deleted node"""
        original = self._validate(p)
        return self._del_node(original)
    
    def replace(self, p, e):
        """returns the old element in the original node"""
        original = self._validate(p)
        old_ele = original.element
        original.element = e
        return old_ele
    
        
    
