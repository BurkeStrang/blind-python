import unittest
from problems.fastandslowpointers.is_happy_number import is_happy_number


class TestHappyNumber(unittest.TestCase):

    def test_example1(self):
        self.assertTrue(is_happy_number(19))

    def test_example2(self):
        self.assertFalse(is_happy_number(3))

    def test_example3(self):
        self.assertTrue(is_happy_number(7))
