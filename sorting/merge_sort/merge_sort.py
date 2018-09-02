from linked_list_queue import LinkedQueue


class Solution():
    def merge(self, s1, s2, s):
        """
        s1, s2: sorted list
        s: list
        """
        i = j = 0
        # while there is still at least an elmenet in s1 or s2
        while i+j < len(s):
            # if all elements in s2 have been put in s;
            # or if there's still some elements in both s1 and s2 and s1[i] < s2[j]
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                s[i+j] = s1[i]
                i+=1
            # if all elements in s1 have been put in s, i.e. i == len(s1)
            # or if there's still some elements in both s1 and s2 and s1[i] > s2[j]
            else:
                s[i+j] = s2[j]
                j+=1

    def merge_sort(self, s):
        l = len(s)
        if l < 2:
            return
        
        mid = l//2
        s1 = s[0:mid]
        s2 = s[mid:l]
        
        self.merge_sort(s1)
        self.merge_sort(s2)
        
        self.merge(s1, s2, s)
    
#######functions to accomplish linked list merge sort######
    def merge_list(self, l1, l2, l):
        while not l1.is_empty() and not l2.is_empty():
            if l1.get_first() < l2.get_first():
                l.enqueue(l1.dequeue())
            else:
                l.enqueue(l2.dequeue())
        while not l1.is_empty():
            l.enqueue(l1.dequeue())
        while not l2.is_empty():
            l.enqueue(l2.dequeue())

    def merge_sort_linked_list(self, l):
        if l.len() < 2:
            return
        
        l1 = LinkedQueue()
        l2 = LinkedQueue()
        
        #move firt half to l1 from l
        while l1.len() < l.len()//2:
            l1.enqueue(l.dequeue())
        #move the rest to l2 from l
        while not l.is_empty():
            l2.enqueue(l.dequeue())
        
        self.merge_sort_linked_list(l1)
        self.merge_sort_linked_list(l2)
        
        self.merge_list(l1, l2, l)
        
    
# test of merge_sort()
s = Solution()
test_list = [93, 3, 2, 8, 123, 1234]
s.merge_sort(test_list)
print(test_list)

# test of merge_sort_linked_list()
l = LinkedQueue()

for ele in test_list:
    l.enqueue(ele)

s.merge_sort_linked_list(l)

while not l.is_empty():
    dequeued_item = l.dequeue()
    print (dequeued_item)
