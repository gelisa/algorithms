import unittest
import sampling_weights as sw
from scipy.stats import ks_2samp, cauchy
from numpy.random import uniform, normal


class Test_Init_Sum(unittest.TestCase):
    def test_sum(self):
        s = sw.Sampler([1, 1, 1])
        self.assertEqual([1, 2, 3], s.s)


class Test_Bin_Search(unittest.TestCase):
    def setUp(self):
        self.s = sw.Sampler([1, 1, 1, 1, 1])

    def test_r1(self):
        self.assertEqual(1, self.s.binary_search(1))

    def test_r2(self):
        self.assertEqual(2, self.s.binary_search(2))

    def test_r05(self):
        self.assertEqual(0, self.s.binary_search(0.5))


class Test_Distributions(unittest.TestCase):
    def test_uniform(self):
        w = [uniform() for i in range(1000)]
        s = sw.Sampler(w)
        output = [w[s.pickIndex()] for i in range(1000)]
        ks, pval = ks_2samp(w, output)
        self.assertGreater(pval, 0.1)

    def test_normal(self):
        w = [abs(normal(1)) for i in range(1000)]
        s = sw.Sampler(w)
        output = [w[s.pickIndex()] for i in range(1000)]
        ks, pval = ks_2samp(w, output)
        self.assertGreater(pval, 0.1)

    # this test should fail rather misirably due to problem sampling from heavy tail
    def test_cauchy(self):
        w = [abs(cauchy(loc=1, scale=10).rvs()) for i in range(1000)]
        s = sw.Sampler(w)
        output = [w[s.pickIndex()] for i in range(10000)]
        ks, pval = ks_2samp(w, output)
        self.assertGreater(pval, 0.1)



if __name__ == '__main__':
    unittest.main()

