class Solution ():
    def insertion_sort(self, input_list):
        """input type: list"""
        count = len(input_list)
        for n in range(count):
            cur = input_list[n]
            j = n
            while j > 0 and input_list [j-1] > cur:
                input_list[j] = input_list [j-1]
                j-=1
            input_list[j] = cur

s = Solution()
test_list = [9, 8, 7, 6, 5, 4]
s.insertion_sort(test_list)
print(test_list)
