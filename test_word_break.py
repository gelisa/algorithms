import unittest
import word_break as wb
import ddt


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.word_dict = {'a', 'aa', 'aaa', 'cat', 'cats', 'and', 'dog', 'dogs', 'sand'}

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_1(self, func):
        self.assertEqual(func('cat', self.word_dict), True)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_2(self, func):
        self.assertEqual(func('anddog', self.word_dict), True)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_3(self, func):
        self.assertEqual(func('catsanddogs', self.word_dict), True)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_overlap(self, func):
        self.assertEqual(func('catsandog', self.word_dict), False)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_repetition(self, func):
        self.assertEqual(func('aaaaaaaaaaaaaaaaaaaa', self.word_dict), True)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_not_in_dict(self, func):
        self.assertEqual(func('bbbbbbbbbddddddbbb', self.word_dict), False)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_double_overlap(self, func):
        self.assertEqual(func('catsanddogsand', self.word_dict), True)

    @ddt.data(wb.wb_dyn_prog, wb.wb_bfs)
    def test_badhead(self, func):
        self.assertEqual(func('bcatcats', self.word_dict), False)



