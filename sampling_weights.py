from random import random


class Sampler:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = sorted(w, reverse=True)
        self.s = self.init_sum()

    def init_sum(self):
        s = []
        cum_sum = 0
        for i in self.w:
            cum_sum = cum_sum + i
            s.append(cum_sum)
        return s

    def binary_search(self, r):
        lo = 0
        hi = len(self.s) - 1
        med = lo + (hi - lo) // 2

        while hi > lo:
            if med == lo:
                return med + (int(self.s[med] <= r))
            elif (self.s[med - 1] <= r) and (self.s[med] > r):
                return med
            elif self.s[med] > r:
                hi = med
                med = lo + (hi - lo) // 2
            else:
                lo = med
                med = lo + (hi - lo) // 2
        return med

    def pickIndex(self):
        """
        :rtype: int
        """
        r = self.s[-1] * random()
        return self.binary_search(r)
