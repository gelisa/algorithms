from random import randint
import logging
from heap import Bin_Heap

logger = logging.getLogger('find_median')


def find_median_short(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return (l[0] + l[1]) / 2


def find_median(l):
    if len(l) <= 2:
        return find_median_short(l)

    heap_size = len(l) // 2 + 1
    bh = Bin_Heap(l[:heap_size])
    min_val = bh.min()
    for item in l[heap_size:]:
        if item <= min_val:
            pass
        else:
            bh.insert(item)
            min_val = bh.min()

    if len(l) % 2 == 0:
        extra_min_val = bh.min()
        return (min_val + extra_min_val) / 2

    return min_val


def pivot_around(p_idx: int, l: list, left, right):
    pivot_val = l[p_idx]
    new_pivot = left
    l[right], l[p_idx] = l[p_idx], l[right]
    for i in range(left, right):
        if l[i] > pivot_val:
            l[i], l[new_pivot] = l[new_pivot], l[i]
            new_pivot += 1
    l[new_pivot], l[right] = l[right], l[new_pivot]
    return new_pivot


def find_max(l, left, right):
    max_val = l[left]
    for i in range(left, right+1):
        if l[i] > max_val:
            max_val = l[i]
    return max_val

def find_min(l, left, right):
    max_val = l[left]
    for i in range(left, right+1):
        if l[i] < max_val:
            max_val = l[i]
    return max_val


def find_median_quick(l):
    if len(l) <= 2:
        return find_median_short(l)

    med_position = len(l) // 2
    logger.debug('median idx {}'.format(med_position))
    left = 0
    right = len(l) - 1
    answer = None
    while left < right:
        logger.debug('left, right: {}, {}'.format(left, right))
        pivot = randint(left, right)
        logger.debug('random pivot {}'.format(pivot))
        new_pivot = pivot_around(pivot, l, left, right)
        logger.debug('list afterv pivoting: {}'.format(l))
        logger.debug('new pivot {}'.format(new_pivot))
        if new_pivot == med_position:
            answer = new_pivot
            break
        elif new_pivot > med_position:
            right = new_pivot - 1
        else:
            left = new_pivot + 1
    if not answer:
        answer = left

    if len(l) % 2 == 0:
        logger.debug('even {}: l[{}] = {}'.format(l, answer, l[answer]))
        extra_min_val = find_min(l, 0, answer - 1)
        logger.debug('extra_value: {}'.format(extra_min_val))
        return (l[answer] + extra_min_val) / 2
    else:
        logger.debug('odd: l[{}] = {}'.format(answer, l[answer]))

    return l[answer]
