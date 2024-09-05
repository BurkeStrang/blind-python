import unittest
import sys

sys.path.append('/home/bstrang/repos/blind-python/problems/twopointers/')

import valid_palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(valid_palindrome.is_palindrome('racecar'))
