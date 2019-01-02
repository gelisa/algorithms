import unittest
import maximum_subarray as ms
import ddt


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(ms.max_subarray_kadane)
    def test_1(self, func):
        self.assertEqual(func([0]), 0)

    @ddt.data(ms.max_subarray_kadane)
    def test_non_neg(self, func):
        arr = [0, 4, 1, 8, 5, 19]
        self.assertEqual(func(arr), sum(arr))

    @ddt.data(ms.max_subarray_kadane)
    def test_non_pos(self, func):
        arr = [-3, -9, -10, -1, -40]
        self.assertEqual(func(arr), max(arr))

    @ddt.data(ms.max_subarray_kadane)
    def test_negative_streak_1(self, func):
        arr = [10, -5, -2, -1, 9]
        self.assertEqual(func(arr), sum(arr))

    @ddt.data(ms.max_subarray_kadane)
    def test_negative_streak_2(self, func):
        arr = [7, -5, -2, -1, 9]
        self.assertEqual(func(arr), 9)

    @ddt.data(ms.max_subarray_kadane)
    def test_negative_head(self, func):
        arr = [-7, -5, -2, 1, 9]
        self.assertEqual(func(arr), 10)

    @ddt.data(ms.max_subarray_kadane)
    def test_negative_tail(self, func):
        arr = [7, 5, -2, -1, -9]
        self.assertEqual(func(arr), 12)



if __name__ == '__main__':
    unittest.main()
