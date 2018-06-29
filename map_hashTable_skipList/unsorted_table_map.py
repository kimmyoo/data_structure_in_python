from map_base import MapBase

class UnsortedTableMap(MapBase):
    """map implemenation using unordered list"""
    # constructor initilizes a list for _Item objects
    # This list-based map implementation is simple, 
    # but it is NOT particularly EFFICIENT!!!!
    # Each of the fundamental methods, getitem, setitem, and delitem, 
    # relies on a for loop to scan the underlying list of items 
    # in search of a matching key.
    def __init__(self):
        self._table = []
    
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError ('Key Error:' + repr(k))
    
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
        self._table.append(self._Item(k, v))
    
    def __delitem__(self, k):
    # delete operation needs to loop throught the
    # entire list and need to handle KeyError
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                # list pop() method
                self._table.pop(j)
                return
        raise KeyError('Key Error:' + repr(k))
    
    def __len__(self):
        return len(self._table)
        
    def __iter__(self):
        for item in self._table:
            yield item._key


#~ # some tests
#~ test_map = UnsortedTableMap()
#~ test_map[0] = 'doudou'
#~ test_map[1] = 'maomao'

#~ for item in test_map:
    #~ print (item, test_map[item])
    
#~ print ("length of the map:", len(test_map))
#~ del test_map[1]
#~ print ("length of the map:", len(test_map))
#~ print (test_map[0])
#~ test_map[0] = "tiaotiao"
#~ print (test_map[0])
    
