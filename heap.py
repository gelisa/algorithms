# binary heap


class Bin_Heap:
    def __init__(self, alist=[]):
        if not alist:
            self.items = [0]
            self.size = 0
        else:
            self.items = self.init_from_list(alist)
            self.size = len(self.items)

    def init_from_list(self, iter: list):
        idx = len(iter) // 2
        items = [0] + iter
        while idx > 1:
            self.perc_up(idx)
            idx -= 1
        return items

    def perc_up(self, cidx: int):
        while self.items[cidx] < self.items[cidx // 2]:
            self.items[cidx], self.items[cidx // 2] = self.items[cidx // 2], self.items[cidx]
            cidx = cidx // 2

    def perc_down(self, cidx: int):
        midx = self.min_child(cidx)
        while self.items[cidx] > self.items[midx]:
            self.items[cidx], self.items[midx] = self.items[midx], self.items[cidx]
            cidx = midx

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.perc_up(self.size - 1)

    def min(self):
        minimum = self.items[1]
        self.size -= 1
        self.perc_down(1)
        return minimum

    def min_child(self, i):
        if self.items[2 * i] > self.items[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1


bh = Bin_Heap()
