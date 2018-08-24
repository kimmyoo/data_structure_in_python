class Solution():
    def merge(self, s1, s2, s):
        i = j = 0
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

s = Solution()
test_list = [93, 3, 2, 8, 123, 1234]
s.merge_sort(test_list)
print(test_list)
