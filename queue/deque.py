from collections import deque


d1 = deque('abcddeque')
# d2 = deque (1234) # must be iterable
print (d1)
print (len(d1))

d1.appendleft('1')
d1.append('0')
print (d1)

d1.pop()
d1.popleft()
print (d1)
print (d1[0], d1[-1])

d1.rotate(1)
print(d1)
d1.remove('d')
print (d1.count('d'), len(d1))
print(d1)


