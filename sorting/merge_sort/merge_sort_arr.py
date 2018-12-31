def mergeSort(inputList):
    length = len(inputList)
    if length < 2:
        return
    
    mid = length//2
    left = inputList[:mid]
    right = inputList[mid:]
    
    mergeSort(left)
    mergeSort(right)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            inputList[k] = left[i]
            i += 1
        else:
            inputList[k] = right[j]
            j += 1
    
        k += 1
    
    while i < len(left):
        inputList[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        inputList[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__': 
    arr = [8, 11, 13, -5, -6, 7]  
    print ("Given array is", end="\n")  
    print(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    print(arr)
