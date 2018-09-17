from linked_queue import LinkedQueue

def quick_sort(t):
    l = len(t)
    if l < 2:
        return
    
    pivot = t.get_first()
    lt = LinkedQueue()
    gt = LinkedQueue()
    et = LinkedQueue()
    
    while not t.is_empty():
        if t.get_first() < pivot:
            lt.enqueue(t.dequeue())
        elif t.get_first() > pivot:
            gt.enqueue(t.dequeue())
        else:
            et.enqueue(t.dequeue())
    
    quick_sort(lt)
    quick_sort(gt)

    #order: less than, equal to, greater than~
    while not lt.is_empty():
        t.enqueue(lt.dequeue())

    while not et.is_empty():
        t.enqueue(et.dequeue())

    while not gt.is_empty():
        t.enqueue(gt.dequeue())


# test
test_q = LinkedQueue()
test_list = [9, 10, 8, 7, 100, 34, 33, 38]
for element in test_list:
    test_q.enqueue(element)

quick_sort(test_q)

while not test_q.is_empty():
    ele = test_q.dequeue()
    print (ele)
    
