import unittest
from problems.twopointers.valid_palindrome import is_palindrome


class TestValidPalindrome(unittest.TestCase):

    def test_example1(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_example2(self):
        self.assertFalse(is_palindrome('hello'))

    def test_example3(self):
        self.assertTrue(is_palindrome('oddo'))
