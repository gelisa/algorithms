



def quickSort(a, pivot):
    """

    :param a:
    :return:
    """
    def get_pivot(pivot, a, l, r):
        """
        :param pivot: can be:
        'first'
        'last'
        'median'
        :return:
        """
        if pivot == 'first':
            return l
        if pivot == 'last':
            return r
        if pivot == 'median':
            three = [(a[l], l), (a[r], r), (a[(r - l) // 2], (r - l) // 2)]
            three.sort(key=lambda x: x[0])
            return three[1][1]
        else:
            raise ValueError('wrong pivot')


    def partition(l, r, p_ind):
        """
        partitioning subroutine for quick solt
        :param l: index, left border of subarray
        :param r: index, right border of subarray
        :return: index of pivot
        """
        nonlocal a
        a[l], a[p_ind] = a[p_ind], a[l]
        p = a[l]
        i = l + 1
        #print(a)
        for j in range(l+1, r+1):
            if a[j] < p:
                a[j], a[i] = a[i], a[j]
                i += 1
        a[l], a[i - 1] = a[i - 1], a[l]

        return i - 1

    def quickSortHelper(l, r, pivot):
        """

        :param l:
        :param r:
        :return:
        """
        nonlocal a
        nonlocal count
        if l < r:
            p_ind = get_pivot(pivot,a,l,r)
            print('pivot',p_ind, a[p_ind])
            p = partition(l, r, p_ind)
            print(count,'->',count+r-l)
            count += r - l
            quickSortHelper(l, p - 1, pivot)
            # if l < p - 1:
            #     count += p - l
            quickSortHelper(p + 1, r, pivot)
            # if r > p + 1:
            #     count += r - p


    if len(a) <=1:
        return None
    count = 0
    quickSortHelper(0,len(a)-1, pivot)
    print(count)

inputs = [[],[1], [1,2], [3,1], [1,6,7,5,3,2,4], [2,4,6,1,3,5]]
outputs = [[],[1],[1,2],[1,3], [1,2,3,4,5,6,7], [1,2,3,4,5,6]]

def testSort(inputs,outputs,function):
    for (i,o) in zip(inputs,outputs):
        function(i)
        if not i == o:
            print('function failed on ',str(i))
            print('expected return is', str(o))
            print('but got ', str(i))
        else:
            print('passed')


def loadData(filename):
    nums = []
    f = open(filename,'r')
    for line in f:
        nums.append(int(line.rstrip('\n')))
    print(nums)
    return nums

#testSort(inputs,outputs,quickSort)

quickSort(loadData('p1w2_10.txt'),'median')
