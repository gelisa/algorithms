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


