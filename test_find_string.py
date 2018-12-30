import unittest
import ddt
import find_string as fs


@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_both_empty(self, func):
        self.assertEqual(func('', ''), [])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_string_empty(self, func):
        self.assertEqual(func('', 'a'), [])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_query_empty(self, func):
        self.assertEqual(func('a', ''), [])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_equal(self, func):
        self.assertEqual(func('a', 'a'), [0])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_repeat_1(self, func):
        self.assertEqual(func('aaa', 'a'), [0, 1, 2])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_repeat_2(self, func):
        self.assertEqual(func('ababab', 'ab'), [0, 2, 4])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_overlap(self, func):
        self.assertEqual(func('abababcabababcc', 'abab'), [0, 2, 7, 9])

    @ddt.data(fs.find_string_bf, fs.boyer_moore)
    def test_end(self, func):
        self.assertEqual(func('ababccab', 'abab'), [0])
