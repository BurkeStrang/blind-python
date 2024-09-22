import unittest
from problems.twopointers.sum_of_three_values import find_sum_of_three


class TestSumOfThreeValues(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(find_sum_of_three(
            [2, 3, 5, 9, 14, 20, 30], 25))

    def test_example2(self):
        self.assertFalse(find_sum_of_three([2, 3, 5, 9, 14, 20, 30], 30))
