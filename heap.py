# binary heap
import logging

logger = logging.getLogger('heap')

class Bin_Heap:
    def __init__(self, alist=[]):
        if not alist:
            self.items = [0]
            self.size = 0
        else:
            self.init_from_list(alist)

    def init_from_list(self, alist: list):
        idx = len(alist) // 2
        logger.debug('init_from_list {}'.format(idx))
        self.size = len(alist)
        self.items = [0] + alist
        while idx > 0:
            logger.debug('init_from_list in while {}'.format(idx))
            self.perc_down(idx)
            idx -= 1

    def perc_up(self, cidx: int):
        while self.items[cidx] < self.items[cidx // 2]:
            self.items[cidx], self.items[cidx // 2] = self.items[cidx // 2], self.items[cidx]
            cidx = cidx // 2

    def perc_down(self, cidx: int):
        logger.debug('perc_down {}'.format(cidx, self.items[cidx]))
        midx = self.min_child(cidx)
        logger.debug('perc_down min child idx {}'.format(midx))
        while self.items[cidx] > self.items[midx]:
            self.items[cidx], self.items[midx] = self.items[midx], self.items[cidx]
            logger.debug('perc_down in while, items {}'.format(self.items))
            cidx = midx

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.perc_up(self.size - 1)

    def min(self):
        minimum = self.items[1]
        self.items[1] = self.items.pop()
        self.size -= 1
        self.perc_down(1)
        return minimum

    def min_child(self, i):
        if self.items[2 * i] < self.items[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1
