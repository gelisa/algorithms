

# b, [x1, x2], [y1, y2]
# abs(b*x1-y1)+abs(b*x2-y2)
# 






def findL1Min(x, y):
    """
    finds a local minimum for the l1 norm
    It is O(nlog(n)) in time and O(n) in space, where n is length of vectors
    O(nlog(n)) comes from sorting
    Parameters:
     x - list of x coordinates
     y - list of y coordinates
    """
    def getZeroBetas(x,y):
        """
        get values of beta at which each of coordinates ||b*x_i-y_i||=0
        return:
         list of tuples [(beta_i, (x_i, y_i)),...]
        """
        betas = []
        for i in range(len(x)):
            # if x = 0, then the objective function doesn't depend on beta
            if not x[i] == 0:
                b = y[i]/x[i]
                betas.append((b, (x[i],y[i])))
        return betas
    n = len(x)
    #first we get betas which deliver 0 to each coordinate
    betas = getZeroBetas(x,y)
    # we sort these values of betas
    betas.sort(key = lambda x: x[0])
    '''
    In between these values objective function is linear in beta (it's a sum of linear functions).
    Thus minima and maxima are achieved at the points wherhe beta delivers 0 to each coordinate.
    There can be a case of flat minimum, then our algorithm delivers left border of it
    '''
    functionVals = []
    '''
    now we caluculate values of objective function in the points
    we calculate input from left absolute values branches and from left ones separately,
    to keep time linear
    '''
    left_x = {}
    left_y = {}
    right_x = {}
    right_y = {}
    #first we sum all the left inputs from x vector and from the right vector
    left_x[n-1] = 0
    left_y[n-1] = 0
    for i in range(n-2,-1,-1):
        left_x[i] = left_x[i+1] + betas[i+1][1][0]
        left_y[i] = left_y[i+1] + betas[i+1][1][1]

    #same for right branches
    right_x[0] = 0
    right_y[0] = 0
    for i in range(1,n):
        right_x[i] = right_x[i-1] + betas[i-1][1][0]
        right_y[i] = right_y[i-1] + betas[i-1][1][1]

    for i in range(len(x)):
        func = (right_x[i] - left_x[i]) * betas[i][0] + left_y[i] - right_y[i]
        functionVals.append((betas[i][0],func))
    #sort, get minima
    functionVals.sort(key = lambda x: x[1])

    #print('betas',betas)
    #print('fv',functionVals)  
    
    return functionVals[0][0]

x = [1,2,2,3]
y = [2,2,1,9]

print(findL1Min(x, y))

