import unittest
from problems.twopointers.sort_colors import sort_colors


class TestSumOfThreeValues(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(sort_colors([2, 1, 0, 1, 2, 0]), [0, 0, 1, 1, 2, 2])

    def test_example2(self):
        self.assertEqual(sort_colors([2, 0, 1]), [0, 1, 2])
