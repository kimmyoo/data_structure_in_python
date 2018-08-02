from binary_search_tree import TreeMap



#creating an TreeMap object called bst
bst = TreeMap()

#test of __setitem__()
bst[1] = 'a'
bst[2] = 'b'
bst[3] = 'c'
bst[0] = 'z'

#test of find_min()
key, value = bst.find_min()
print (key, value)

#test of __getitem__()
print (bst[0])

#test of first() and last()
print (bst.first().element()._value, bst.last().element()._value)

#test of __delitem__()
del bst[0]
key, value = bst.find_min()
print (key, value)

#test of __iter__()
for key in bst:
    print ('-------')
    print (key, bst[key])
    
#test of find_position
print (bst.find_position(1).value())
print (bst.find_position(0).value())

rcptr = bst.find_ge(4)
print (rcptr)

#test of inorder, postorder, and preorder methods inherited 
#from BinaryTree class
for p in bst.inorder():
    print (p.element()._value)
print('-----')
for p in bst.postorder():
    print (p.element()._value)

#def inorder_display()
def inorder_display():
    for p in bst.preorder():
        print (p.element()._value)
        if p is not None:
            if bst.right(p) is None:
                print("no right child")
            else:
                print("right child:", bst.right(p).element()._value)
            if bst.left(p) is None:
                print("no left child")
            else:
                print("left child:", bst.left(p).element()._value)

print('-----test of _restructure()')
for p in bst.preorder():
    print (p.element()._value)
    if p.element()._value == 'c':
        pivot = p
    if p is not None:
        if bst.right(p) is None:
            print("no right child")
        else:
            print("right child:", bst.right(p).element()._value)
        if bst.left(p) is None:
            print("no left child")
        else:
            print("left child:", bst.left(p).element()._value)
print('-----after _restructure(), inorder display')
newroot = bst._restructure(pivot)
inorder_display()
