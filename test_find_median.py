import unittest
from find_median import find_median


class Test(unittest.TestCase):
    def test_0(self):
        self.assertIsNone(find_median([]))

    def test_1(self):
        self.assertEqual(0, find_median([0]))

    def test_2(self):
        self.assertEqual(1, find_median([0, 1]))

    def test_3(self):
        self.assertEqual(1, find_median([0, 1, 2]))

    def test_4(self):
        self.assertEqual(2, find_median([0, 1, 2, 3]))

    def test_some_equal(self):
        self.assertEqual(1, find_median([0, 1, 1, 2, 3]))

    def test_inverse(self):
        self.assertEqual(3, find_median([5, 4, 3, 2, 1]))

    def test_unsorted(self):
        self.assertEqual(3, find_median([1, 3, 4, 5, 2]))


if __name__ == '__main__':
    unittest.main()

