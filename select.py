"""
implements a linear in time quick select algorithm
"""

import random

def subPartition(array, first, last):
    l = len(array)
    pivot = first
    left = pivot + 1
    right = last
    done = False
    
    while not done:
        while left <= right:
            if array[left] < array[pivot]:
                left+=1
            else:
                break

        while left <= right:
            if array[right] > array[pivot]:
                right -= 1
            else:
                break

        if left > right:
            done = True
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot], array[right] = array[right], array[pivot]

    return right
    
def quickSortHelper(array, first, last):
    if first < last:
        splitPoint = subPartition(array, first, last)

        quickSortHelper(array, first, splitPoint-1)
        quickSortHelper(array, splitPoint+1, last)
        
    return None

def quickSort(array):
    quickSortHelper(array,0,len(array)-1)
    return array

def quickSelect(array,i):
    splitPoint = subPartition()
    if i < pivot
    
    return None


assert quickSort([0,1,2,3]) == [0,1,2,3]
assert quickSort([]) == []
assert quickSort([1]) == [1]
assert quickSort([1,4,0,2,3]) == [0,1,2,3,4]
assert quickSort([0,5,4,2,3,1]) == [0,1,2,3,4,5]

