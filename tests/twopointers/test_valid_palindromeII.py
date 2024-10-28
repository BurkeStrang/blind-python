import unittest
from problems.twopointers.valid_palindromeII import is_palindromeII


class TestValidPalindrome(unittest.TestCase):

    def test_example1(self):
        self.assertTrue(is_palindromeII('raceacar'))

    def test_example2(self):
        self.assertFalse(is_palindromeII('hello'))

    def test_example3(self):
        self.assertTrue(is_palindromeII('odao'))
