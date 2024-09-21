import unittest
from problems.twopointers.valid_palindrome import is_palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(is_palindrome('racecar'))
