# 15:34 -> 16:05
# 
import re
from collections import defaultdict

def removeDuplicates(string):
    tmpString = re.sub(r'[,|.]',r' ',string)
    return ' '.join(set(tmpString.split(' ')))

def rmDupNoRe(string):
    tmpList = string.split(' ')
    punct = [',','.']
    for punctSign in punct:
        tmpList = [word.rstrip(punctSign) for word in tmpList]
    return ' '.join(set(tmpList))

def rmDup2(string):
    table = {r',': r' ',r'.':r' ',';':' '}
    noPunct = string.translate(string.maketrans(table))
    return ' '.join(set(noPunct.split(' ')))

def testRm():
    str1 = 'str tmp,why. tmp and none str'
    print(removeDuplicates(str1))
    print(rmDupNoRe(str1))
    print(rmDup2(str1))

def mergeArrays(arr1,arr2):
    # [0, 1, 2] [2, 3, 4]
    # [1, 3, 5] [2, 4, 6, 8]
    if arr1[-1] <= arr2[0]:
        return arr1 + arr2
    elif arr2[-1] <= arr2[0]:
        return arr2 + arr1
    else:
        la1 = len(arr1)
        la2 = len(arr2)
        mergeArr = [0]*(la1+la2)
        i = 0
        j = 0
        k = 0
        while i < la1 and j < la2:
            if arr1[i] <= arr2[j]:
                mergeArr[k] = arr1[i]
                i += 1
                k += 1
            else:
                mergeArr[k] = arr2[j]
                j += 1
                k += 1
        while i < la1:
            mergeArr[k] = arr1[i]
            k += 1
            i += 1
        while j < la2:
            mergeArr[k] = arr2[j]
            k += 1
            j += 1
    return mergeArr

def testMerge():
    arr1 = [1,3,5]
    arr2 = [2,4,6,8]
    arr3 = [0,0,3,4]
    arr4 = [0,1]
    print(mergeArrays(arr1,arr2))
    print(mergeArrays(arr1,arr4))
    print(mergeArrays(arr3,arr1))

def findMax(dictParam):
    newDict = defaultdict(int)
    for key,value in dictParam.items():
        newDict[key[0]] += value
        newDict[key[1]] -= value

    tuples = [(k,v) for k, v in newDict.items()]
    tuples.sort(key = lambda tup: tup[0])
    l = [tup[1] for tup in tuples]
    maxSum = 0
    currSum = 0
    nl = len(l)
    for j in range(0,nl):
        currSum += l[j]
        if currSum > maxSum:
            maxSum = currSum
    return maxSum

def testFindMax():
    dictParam = {(1,3):1,(2,5):4,(6,7):10,(0,1):2,(2,3):1}
    print(findMax(dictParam))
