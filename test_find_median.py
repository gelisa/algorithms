import unittest
import find_median as fm
import ddt

@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_0(self, func):
        self.assertIsNone(func([]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_1(self, func):
        self.assertEqual(0, func([0]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_2(self, func):
        self.assertEqual(0.5, func([0, 1]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_3(self, func):
        self.assertEqual(1, func([0, 1, 2]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_4(self, func):
        self.assertEqual(1.5, func([0, 1, 2, 3]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_some_equal(self, func):
        self.assertEqual(1, func([0, 1, 1, 2, 3]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_inverse(self, func):
        self.assertEqual(3, func([5, 4, 3, 2, 1]))

    @ddt.data(fm.find_median, fm.find_median_quick)
    def test_unsorted(self, func):
        self.assertEqual(3, func([1, 3, 4, 5, 2]))


if __name__ == '__main__':
    unittest.main()

