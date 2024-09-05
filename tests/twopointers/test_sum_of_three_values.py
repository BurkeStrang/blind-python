import unittest
import sys

sys.path.append('/home/bstrang/repos/blind-python/problems/twopointers/')

import sum_of_three_values


class TestSumOfThreeValues(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(sum_of_three_values.find_sum_of_three([2, 3, 5, 9, 14, 20, 30], 25))
