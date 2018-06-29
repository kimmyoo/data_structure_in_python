from binarytree import BinaryTree

class LinkedBinaryTree (BinaryTree):
    class _Node: 
        __slots__= '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    #BinaryTree class actually inherited Position class from Tree base class
    class Position(BinaryTree.Position):
        """Position class contains atributes and methods for validation"""
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type (other) is type (self) and other._node is self._node
    
    def _validate(self, p):
        """unwrap a node for use"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p doesn\'t belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        '''wrap a node'''
        #~ if node is not None:
            #~ return self.Position(self, node)
        #~ else:
            #~ return None
        return self.Position(self, node) if node is not None else None
    
    #------binary tree constructor
    def __init__ (self):
        self._root = None
        self._size = 0
    
    # ------public accessors
    
    # is_root(), is_leaf(), and is_empty() were implemented in the base class
    def __len__(self):
        return self._size
    
    def root(self):
        """returns an instance of a Position instead of a node"""
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        # _make_position return None if Node is a None
        # so if node is root, root.parent is None, so this method will return 
        # none if p is unwrapped to be root
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        #first check if root exists
        if self._root is not None: raise ValueError('Root exists!')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        '''returns position of the new node'''
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        node._left = self._Node(e, node) # node is node._left's parent
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        '''returns position of the new node'''
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
        node._right = self._Node(e, node) # node is node._left's parent
        self._size += 1
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        '''returns old element stored in original position'''
        node = self._validate(p)
        old_element = node._element
        node._element = e
        return old_element
        
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children == 2:
            raise ValueError ('p has 2 children')
        #this only test if left or right exists
        child = node._left if node._left else node._right #child might be None
        if child is not None:
            child._parent = Node._parent # child connects to grandparent 
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:  #deletion happens on left branch of 
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deprecated node
        return node._element
    
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf!')
        if not type(self) is type (t1) is type(t2):
            raise TypeError('tree types must match')
            
        self._size = len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # set t1 to empty
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


