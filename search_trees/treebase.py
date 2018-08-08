from queue import ArrayQueue

class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
            
        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """return the root of the tree"""
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        """get p's parent"""
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        """return number of p's children"""
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    # pay attention to the len() and __len__q
    def is_empty(self):
        return len(self) == 0
        
    # recursive way to find node's depth: 
    # The depth of p is the number of 
    # ancesters of p, excluding p itself.
    # 一想到 height 或者 depth, 就要想到是recursive
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    # node's height
    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+ max(self.height(child) for child in self.children(p))

# implementation of the default iteration method of a tree
    def __iter__(self):
        '''generate an iteration of the tree's element'''
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder() # choose the default iteration 

# tree traversals: preorder, postorder
    # using generator: generate position objects on the fly
    # memory efficient
    # the generator yields position object and let the caller of the 
    # generator decide what to do with the position
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # start recursion 
                yield p

    def _subtree_preorder(self, p):
        yield p # pre
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for child in self.children(p):
            for other in self._subtree_postorder(child):
                yield other
        yield p # post

# breadth first traversal
    def breadthfirst(self):
        if not self.is_empty():
            fringe = ArrayQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for child in self.children(p):
                    fringe.enqueue(child)

# in-order traversal was implemented in the binarytree module
    

