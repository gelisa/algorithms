

def bubbleSort():
    return None

def selectionSort():
    return None

def insertionSort():
    return None

def shellSort():
    return None

def mergeSort():
    return None

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
