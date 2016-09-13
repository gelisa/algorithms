

def bubbleSort():
    return None

def selectionSort():
    return None

def insertionSort():
    return None

def shellSort():
    return None

def mergeSort(alist):
    """
    performs a merge sort
    :param alist: list of numbers
    :return: sorted list of numbers
    """
    if alist == []:
        return []
    if len(alist) == 1:
        return alist
    else:
        left = mergeSort(alist[0:len(alist)//2])
        right = mergeSort(alist[len(alist)//2:])
    mergeList = []
    i = 0
    j = 0
    while ( i < len(left)) and ( j < len(right)):
        if left[i] < right[j]:
            mergeList.append(left[i])
            i += 1
        else:
            mergeList.append(right[j])
            j += 1
    if i < len(left):
        mergeList += left[i:]
    if j < len(right):
        mergeList += right[j:]
    return mergeList

def quickSort(alist):
    def partition(alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp


       return rightmark

    
    def quickSortHelper(alist,first,last):
        print(alist)
        if first<last:
            splitpoint = partition(alist,first,last)
            print('split at',splitpoint)
            

            quickSortHelper(alist,first,splitpoint-1)
            quickSortHelper(alist,splitpoint+1,last)
    
    quickSortHelper(alist,0,len(alist)-1)
    
    return None

def heapSort():
    return None

def timSort():
    return None

inputs = [[],[1], [1,2], [3,1], [1,3,2], [2,4,6,1,3,5]]
outputs = [[],[1],[1,2],[1,3],[1,2,3], [1,2,3,4,5,6]]

def testSort(inputs,outputs,function):
    for (i,o) in zip(inputs,outputs):
        io = function(i)
        if not io == o:
            print('function failed on ',str(i))
            print('expected return is', str(o))
            print('but got ', str(io))
        else:
            print('passed')

testSort(inputs,outputs,mergeSort)