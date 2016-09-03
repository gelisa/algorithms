from collections import defaultdict


def fibRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

def fibIter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def matrixIter(dimArray):
    """
    we have matrices, say 2x3, 3x4, 4x5
    it is required to know what is the smallest number
    of operations can be used to multiply them
    dimArray -- [int] is the array of the sizes of the matrix,
    in the case above it will be [2,3,4,5]
    it is solved by finding solutitions of subproblems first
    """
    a = defaultdict(int) # here we store solutions of the subproblems
    s = len(dimArray)
    for k in range(1,s):
        # for the case above k = 1,2,3
        # k is a gap between a first index of dimArray and the last
        # for which we searching a solution of a subproblem
        for i in range(0,s-k):
            #first index of a subproblem is called i, the last is j
            j = i + k
            if j - i == 1:
                a[(i, j)] = 0
            elif j - i == 2:
                a[(i, j)] = dimArray[i] * dimArray[i+1] * dimArray[j]
                print(i,j,":",a[(i, j)])
            else:
                listTmp = []
                for t in range(i+1, j):
                    print(i,t,j,":",a[(i,t)],a[(t,j)],dimArray[i] * dimArray[t] * dimArray[j])
                    listTmp.append(a[(i, t)] + a[(t, j)] + dimArray[i] * dimArray[t] * dimArray[j])
                print(i,j,listTmp)
                a[(i, j)] = min(listTmp)
    print(a)
    return a[(0, s-1)]


def trainRec(i,j,priceDict,prices={}):
    '''i-th station, j-th station,
    priceDict -- dict of known prices
    prices -- dict to store already calculated min prices
    '''
    if j - i <= 0:
        #print(i,j,0)
        return 0
    if j - i == 1:
        return priceDict[(i,j)]
    else:
        priceList = []
        try:
            return prices[(i,j)]
        except KeyError:
            try:
                priceList.append(priceDict[(i,j)])
            except KeyError:
                pass
            for k in range(i+1,j):
                priceList.append(trainRec(i,k,priceDict,prices)+trainRec(k,j,priceDict,prices))
            print(priceList)
            prices[(i,j)] = min(priceList)
            print(prices)
        return prices[(i,j)]

def testTrain():
    pl = {(0, 1): 3, (0, 2): 6, (0, 3): 8, (1, 2): 3, (2, 3): 4, (2, 4): 7, (3, 4): 2}
    print(trainRec(0,4,pl))

def ifSum(array,n):
    l = len(array)
    if l == 0:
        return False
    else:
        oldSum = set([0])
        for i in range(l):
           x = array[i]
           print(i,x,': sum',oldSum)
           tmp = set([])
           for num in oldSum:
               s = x + num
               print(i,s)
               if s < n:
                   tmp.add(s)
               elif s == n:
                   return True
               else:
                   continue
               print('tmp',tmp)
           oldSum = oldSum.union(tmp)
    return False

def hanoiRec(i,m,n):
    '''
    i - num of rings
    m - move from this ring
    n = move to this ring
    '''
    if i == 1:
        print('move from ',m,' to ',n)
    else:
        s = 6 - m - n
        hanoiRec(i-1, m, s)
        print('Move from ',m, ' to ', n)
        hanoiRec(i-1,s,n)

def hanoiStack(i, m, n,):
    stack = []
    stack.append((i,m,n))
    while not stack == []:
        j, p, q =  stack.pop()
        if j == 1:
            print('move from',p,'to',q)
        else:
            s = 6 - p - q
            stack.append((j-1, s, q))
            stack.append((1, p, q))
            stack.append((j-1, p, s))

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        if not self.left == None:
            left = self.left.val
        else:
            left = None
        if not self.right == None:
            right = self.right.val
        else:
            right = None
        return(str(self.val)+' : '+str(left)+' <- -> '+str(right))

    def __repr__(self):
        return self.__str__()
        
    def postOrderRec(self,root):
        '''
        root -> TreeNode
        post order: let, right, root
        '''
        result = []
        def recurse(node):
            if not node:
                return None
            else:
                recurse(node.left)
                recurse(node.right)
                result.append(node.val)
        recurse(root)
        return result

    def postOrderStack(self,root):
        result = []
        stack = []
        stack.append((False,root))
        while not stack == []:
            state, node = stack.pop()
            if node == None:
                continue
            if state == True:
                result.append(node.val)
                continue
            if node.left == None:
                if node.right == None:
                    stack.append((True, node))
                else:
                    stack.append((True, node))
                    stack.append((False, node.right))
            else:
                if node.right == None:
                    stack.append((True, node))
                    stack.append((False, node.left))
                else:
                    stack.append((True, node))
                    stack.append((False, node.right))
                    stack.append((False, node.left))
            
            
        return result

    def preOrderStack(self,root):
        def addNone(result,node):
            if not node == None:
                result.append(node.val)
        def stackNode(stack,node):
            if not node == None:
                stack.append(node)
                
        result = []
        stack = []
        stack.append(root)
        while not stack == []:
            node = stack.pop()
            addNode(result,node)
            stackNode(stack,node.right)
            stackNode(stack,node.left)

def quickSortStack(alist):
    def partition(alist, first, last):
        pivot = alist[first]
        left = first + 1
        right = last
        done = False
        while not done:
            #print(0)
            while left <= right and alist[left] <= pivot:
                left = left + 1
                #print(1)

            while alist[right] >= pivot and right >= left:
                #print('l',left,'r',right)
                right = right - 1
                #print(2)

            if right < left:
                done = True
            else:
                alist[left], alist[right] = alist[right], alist[left]
        #print('flr',first,left,right)
        alist[first], alist[right] = alist[right], alist[first]

        return right
    
    stack = []
    firstPoint = 0
    lastPoint = len(alist) -1
    stack.append((firstPoint, lastPoint))
    while not stack == []:
        #print(3)
        #print(stack)
        first, last = stack.pop()
        print(alist)
        if first < last:
            splitPoint = partition(alist, first, last)
            #print('split at',splitPoint)

            if splitPoint - first > last - splitPoint:
                stack.append((first,splitPoint-1))
                stack.append((splitPoint,last))
            else:
                stack.append((splitPoint+1,last))
                stack.append((first,splitPoint-1))
    

def recurse1(x,a,h,l):
    '''
    x -- natural number
    h -- know function natural num -> natural num
    l -- know decreasing function nat num -> nat num
    
    '''
        
    stack = []
    funcStack = []
    if x == 0:
        return a
    else:
        x_i = x
        stack.append(x_i)
        while not x_i == 0:
            x_i = l(x_i)
            stack.append(x_i)
        print('stack',stack)
        funcStack.append(a)
        while not stack == []:
            x_j = stack.pop()
            f_j = funcStack.pop()
            print('x f',x_j,f_j)
            funcStack.append(h(x_j,f_j))
        print(funcStack)
    return funcStack.pop()

def l(x):
    if x>=1:
        return x - 1
    else:
        return None

def r(x):
    if x>=2:
        return x - 2
    else:
        return None

def h(x,f):
    return x + f

def makeTree(x,l,r):
    def recurse(node):
        if node.val > 0:
            if not l(node.val) == None:
                node.left = TreeNode(l(node.val))
                recurse(node.left)
            if not r(node.val) == None:
                node.right = TreeNode(r(node.val))
                recurse(node.right)
            print(node)
    
    root = TreeNode(x)
    recurse(root)
    
    return root
        

def recurse2recursive(x,a,l,r,h):
    root = makeTree(x,l,r)
    result = root.postOrderStack(root)
    return result


            
