import unittest
from problems.twopointers.reverse_words import reverse_words


class TestSumOfThreeValues(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(reverse_words("Hello, world!"), "world! Hello,")

    def test_example2(self):
        self.assertEqual(reverse_words("The quick brown fox"),
                         "fox brown quick The")
