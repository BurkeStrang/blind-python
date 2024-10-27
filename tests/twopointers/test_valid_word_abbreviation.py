import unittest
from problems.twopointers.valid_word_abbreviation import valid_word_abbreviation


class TestValidWordAbbreviation(unittest.TestCase):

    def test_example1(self):
        self.assertTrue(valid_word_abbreviation(
            'internationalization', 'i12iz4n'))

    def test_example2(self):
        self.assertFalse(valid_word_abbreviation(
            'apple', 'a2e'))

    def test_example3(self):
        self.assertFalse(valid_word_abbreviation(
            'word', 'w0rd'))

    def test_example4(self):
        self.assertTrue(valid_word_abbreviation(
            'calendar', 'c6r'))
