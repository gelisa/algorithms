
import unittest
from heap import Bin_Heap


class Test(unittest.TestCase):
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

    def test_init_unordered(self):
        alist = [2, 1, 3]
        bh = Bin_Heap(alist)
        self.assertEqual(bh.items, [0, 1, 2, 3])
        self.assertEqual(bh.size, len(alist))

    def test_init_reverse(self):
        alist = [5, 4, 3, 2, 1]
        bh = Bin_Heap(alist)
        self.assertEqual(bh.items, [0, 1, 2, 3, 5, 4])
        self.assertEqual(bh.size, len(alist))

    def test_insert_big(self):
        alist = [1,2,3]
        bh = Bin_Heap(alist)
        bh.insert(4)
        self.assertEqual(bh.items, [0, 1, 2, 3, 4])
        self.assertEqual(bh.size, 4)

    def test_insert_small(self):
        alist = [1,2,3]
        bh = Bin_Heap(alist)
        bh.insert(0)
        self.assertEqual(bh.items, [0, 0, 1, 3, 2])
        self.assertEqual(bh.size, 4)

    def test_min(self):
        alist = [5, 4, 3, 2, 1]
        bh = Bin_Heap(alist)
        minimum = bh.min()
        self.assertEqual(bh.items, [0, 2, 4, 3, 5])
        self.assertEqual(bh.size, 4)
        self.assertEquals(minimum, 1)


if __name__ == '__main__':
    unittest.main()


