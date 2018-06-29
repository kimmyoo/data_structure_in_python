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
