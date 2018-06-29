from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        return bucket[k]
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        #deal with newly added item in bucket and update self._n
        oldsize = len(self._table[j])
        #set newly added item; an update of value with the same key 
        #will not affect self._n
        self._table[j][k] = v
        if len(self._table)>oldsize:
            self._n += 1
        
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError ('Key Error:' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

# test code for ChainHashMap class
chm = ChainHashMap()
chm.__setitem__(1, 'w.y.')
chm.__setitem__(10, 'Hell0')

receptor = chm.__getitem__(10)
print (receptor)
receptor = chm.__getitem__(1)
print (receptor)
print (chm._n)

chm.__delitem__(1)
print(chm._n)


