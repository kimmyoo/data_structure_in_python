#unoptimized 
def bubbleSort (inputList):
    len_of_list = len(inputList)
    #counter is used to see how many times of comparison will be performed
    counter = 0
    for i in range (len_of_list - 1):
        swapped = False
        #this for loop keeps the current large element moving to right
        for j in range (len_of_list-1):
            counter += 1
            if inputList[j] > inputList[j+1]:
                temp = inputList[j]
                inputList[j] = inputList[j+1]
                inputList [j+1] = temp
                swapped = True
        print (len_of_list)
        if not swapped:
            break
    print(counter)


#optimized
def optBubbleSort(inputList):
    len_of_list = len(inputList)
    counter = 0
    for i in range (len_of_list - 1):
        swapped = False
        #the inner loop can be optimized when observing 
        #that the n-th pass finds the n-th largest element and
        #puts it into its final place, so there is no need to perform 
        #comparison for the last n-1 elements
        for j in range (len_of_list -1):
            counter += 1
            if inputList[j] > inputList [j+1]:
                temp = inputList[j]
                inputList[j] = inputList[j+1]
                inputList[j+1] = temp
                swapped = True
        len_of_list -= 1
        print (len_of_list)
        if not swapped:
            break
    print(counter)



testListA = [9, 9, 10, 0, 1, 2, 77, -100]
testListB = [8, 9, 10, 0, 1, 2, 77, -100]
print ("original listA:", testListA)
print ("\noriginal listB:", testListB)
bubbleSort(testListA)
optBubbleSort(testListB)
print(testListA)
print(testListB)
