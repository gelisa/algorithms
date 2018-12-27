import unittest
from find_median import find_median


class Test(unittest.TestCase):
    def test_0(self):
        l = []
        self.assertIsNone(find_median(l))

    def test_1(self):
        l = [0]
        self.assertEqual(l[0], find_median(l))

    def test_2(self):
        l = [0, 1]
        self.assertEqual(1, find_median(l))

    def test_3(self):
        l = [0, 1, 2]
        self.assertEqual(1, find_median(l))

    def test_4(self):
        l = [0, 1, 2, 3]
        self.assertEqual(2, find_median(l))

    def test_some_equal(self):
        l = [0, 1, 1, 2, 3]
        self.assertEqual(1, find_median(l))

    def test_inverse(self):
        self.assertEqual(3, find_median([5, 4, 3, 2, 1]))

    def test_inverse(self):
        self.assertEqual(3, find_median([5, 4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()

