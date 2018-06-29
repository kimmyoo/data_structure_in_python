from treebase import Tree

class BinaryTree(Tree):
    def left(self, p):
        """p's left child"""
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        """p's right child"""
        raise NotImplementedError('must be implemented by subclass')
    
    def sibling(self, p):
        """returns sibling of p"""
        parent = self.parent(p)
        if parent == None:
            return None
        else:
            if p == self.left(p):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self, p):
        """implemented with left() and right()"""
        #You use is (and is not) for singletons, like None, where you 
        #don't care about objects that might want to pretend to be None 
        #or where you want to protect against objects breaking when 
        #being compared against None.
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

# inorder traversal: 
# it's especially important when the tree is binary search tree
# the in-orde traversal will visit each node according to a particular order
    def inorder (self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

