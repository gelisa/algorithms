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
        logger.debug('init_from_list idx {}'.format(idx))
        self.size = len(alist)
        self.items = [0] + alist
        while idx > 0:
            logger.debug('init_from_list in while h[{}]={}'.format(idx, self.items[idx]))
            self.perc_down(idx)
            idx -= 1

    def perc_up(self, cidx: int):
        while cidx // 2 > 0:
            if self.items[cidx] < self.items[cidx // 2]:
             self.items[cidx], self.items[cidx // 2] = self.items[cidx // 2], self.items[cidx]
            cidx = cidx // 2

    def perc_down(self, cidx: int):
        while cidx * 2 <= self.size:
            logger.debug('perc_down h[{}]={}'.format(cidx, self.items[cidx]))
            midx = self.min_child(cidx)
            logger.debug('perc_down min child h[{}]={}'.format(midx, self.items[midx]))
            if self.items[cidx] > self.items[midx]:
                self.items[cidx], self.items[midx] = self.items[midx], self.items[cidx]
                logger.debug('perc_down in while, items {}'.format(self.items))
            cidx = midx

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.perc_up(self.size)

    def min(self):
        if self.size == 0:
            raise IndexError('Heap size is 0')
        if self.size == 1:
            self.size = 0
            return self.items[1]

        minimum = self.items[1]
        self.items[1] = self.items.pop()
        self.size -= 1
        self.perc_down(1)
        return minimum

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.items[2 * i] < self.items[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1
