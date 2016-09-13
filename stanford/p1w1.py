# assignment for part 1 week 1
# number of inversions



def countInversions(alist):
    """

    :return:
    """

    def mergeSort(alist):
        """
        performs a merge sort
        :param alist: list of numbers
        :return: sorted list of numbers
        """
        nonlocal counts
        if alist == []:
            return []
        if len(alist) == 1:
            return alist
        else:
            left = mergeSort(alist[0:len(alist) // 2])
            right = mergeSort(alist[len(alist) // 2:])
        mergeList = []
        i = 0
        j = 0
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                mergeList.append(left[i])
                i += 1
            else:
                mergeList.append(right[j])
                j += 1
                counts += len(left)-i
        if i < len(left):
            mergeList += left[i:]
        if j < len(right):
            mergeList += right[j:]
        return mergeList
    counts = 0
    mergeSort(alist)

    return counts

inputs = [[],[1], [1,2], [3,1], [1,3,2], [2,4,6,1,3,5],[2,1,4,3],[4,3,2,1]]
outputs = [0,0,0,1,1,6,2,6]

def test(inputs,outputs,function):
    for (i,o) in zip(inputs,outputs):
        io = function(i)
        if not io == o:
            print('function failed on ',str(i))
            print('expected return is', str(o))
            print('but got ', str(io))
        else:
            print('passed')

def loadData():
    nums = []
    f = open('p1w1.txt','r')
    for line in f:
        nums.append(int(line.rstrip('\n')))
    return nums

#test(inputs,outputs,countInversions)
print(countInversions(loadData()))


