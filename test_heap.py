
import unittest
from heap import Bin_Heap


class Init_Test(unittest.TestCase):
    def setUp(self):
        self.bh_none = Bin_Heap()
        self.bh_empty = Bin_Heap([])

    def _test_init(self, bh):
        self.assertEqual(bh.items, [0])
        self.assertEqual(bh.size, 0)

    def test_init_none(self):
        self._test_init(self.bh_none)

    def test_init_empty(self):
        self._test_init(self.bh_empty)

    def test_init_ordered(self):
        alist = [1, 2, 3]
        bh = Bin_Heap(alist)
        self.assertEqual(bh.items, [0, 1, 2, 3])
        self.assertEqual(bh.size, len(alist))

    def test_itit_unordered_1(self):
        alist = [2, 1, 3]
        bh = Bin_Heap(alist)
        self.assertEqual(bh.items, [0, 1, 2, 3])
        self.assertEqual(bh.size, len(alist))


if __name__ == '__main__':
    unittest.main()


