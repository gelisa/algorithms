

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)


def power_log(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return a * 2 * power_log(a, n/2)
    else:
        return a * power_log(a, n-1)


def tree_counter(l, r, x):
    if l[x] == -1 and r[x] == -1:
        return 1
    else:
        return tree_counter(l,r,l[x])+tree_counter(l,r,r[x])+1

def leaf_counter(l, r, x):
    if l[x] == -1 and r[x] == -1:
        return 1
    else:
        return leaf_counter(l,r,l[x])+leaf_counter(l,r,r[x])

def get_n_depth(l, r, x, n):
    counter = [0]
    def get_tree_depth(l,r,x,counter):
        if l[x] == -1 and r[x] == -1:
            return 0
        else:
            leftd = get_tree_depth(l,r,l[x],counter)
            if leftd == n:
                counter[0] += 1
            rightd = get_tree_depth(l,r,r[x],counter)
            if rightd == n:
                counter[0] += 1
            return max(leftd, rightd)+1
    get_tree_depth(l,r,x,counter)
    return counter[0]




l = [-1,-1,0,-1,5,-1,6]
r = [-1,-1,4,2,1,-1,6]


print(tree_counter(l,r,2))
print(leaf_counter(l,r,2))
# print(get_tree_depth(l,r,2))
print(get_n_depth(l,r,2,2))




