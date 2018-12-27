from random import randint
from heap import Bin_Heap


def find_median(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)

    if len(l) % 2:
        heap_size = len(l) // 2 + 1
    else:
        heap_size = len(l) // 2
    bh = Bin_Heap(l[:heap_size])
    min_val = bh.min()
    for item in l[heap_size:]:
        if item <= min_val:
            pass
        else:
            bh.insert(item)
            min_val = bh.min()
    return min_val


def pivot_around(p_idx: int, l: list, left, right):
    pivot_val = l[p_idx]
    new_pivot = left
    l[right], l[p_idx] = l[p_idx], l[right]
    for i in range(right):
        if l[i] > pivot_val:
            l[i], l[new_pivot] = l[new_pivot], l[i]
            new_pivot += 1
    l[new_pivot], l[right] = l[right], l[new_pivot]
    return new_pivot


def find_median_quick(l): # TODO fix bugs
    med_position = len(l) // 2
    print('mp', med_position)
    left = 0
    right = len(l) - 1
    while left < right:
        pivot = randint(0, len(l) - 1)
        new_pivot = pivot_around(pivot, l, left, right)
        print('np', new_pivot)
        if new_pivot == med_position:
            return l[new_pivot]
        elif new_pivot > med_position:
            right = new_pivot - 1
        else:
            left = new_pivot + 1