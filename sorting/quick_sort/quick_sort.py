def quick_sort(input_list):
    if len(input_list) < 2:
        return
    #select pivot element
    pivot = input_list[0]
    lt_list = []
    gt_list = []
    et_list = []
    
    #divide 
    while len(input_list) != 0:
        if input_list[0] > pivot:
            gt_list.append(input_list.pop(0))
        if input_list[0] < pivot:
            lt_list.append(input_list.pop(0))
        else:
            et_list.append(input_list.pop(0))
    
    #conquer: to recursively sort each sublist out
    quick_sort(lt_list)
    quick_sort(gt_list)
    
    #merge back
    while len(lt_list) != 0:
        input_list.append(lt_list.pop(0))
    while len(et_list) != 0:
        input_list.append(et_list.pop(0))
    while len(gt_list) != 0:
        input_list.append(gt_list.pop(0))



test_list = [13, 6, 0, 1, -1, -9]
quick_sort(test_list)
print (test_list)
