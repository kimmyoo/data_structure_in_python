from heapq  import heappush, heappop

def heapsort(input_list):
    h = []
    for item in input_list:
        heappush(h, item)
    return [heappop(h) for i in range (len(h))]


input = [5, 8, 3, 0, -1, 100, 99]
print (heapsort(input))

