



class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
                i = i // 2
            else:
                break

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def minChild(self,i):
        if self.heapList[2*i] > self.heapList[2*i+1]:
            return 2 * i
        else:
            return 2 * i + 1    
        
    def percDown(self,i):
        while i * 2 <= self.currentSize:
            self.heapList[i], self.heapList[self.minChild(i)] =  self.heapList[self.minChild(i)], self.heapList[i]

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        

bh = BinHeap()
for item in [1,2,3,8,4,7,0,5]:
    bh.insert(item)
    print(bh.heapList)
