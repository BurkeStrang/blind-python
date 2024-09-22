# Given a sentence,
# reverse the order of its words
# without affecting the order of letters within the given word.
#
# Constraints:
# The sentence contains English uppercase and lowercase letters,
# digits, and spaces.
#
# 1 ≤ sentence.length ≤ 10^4
# The order of the letters within a word is not to be reversed.
#
# Example 1:
# Input: "Hello, world!"
# Output: "world! Hello,"
#
# Example 2:
# Input: "The quick brown fox"
# Output: "fox brown quick The"

import re


def reverse_words(sentence):
    # Remove extra spaces and strip leading/trailing spaces
    sentence = re.sub(' +', ' ', sentence.strip())

    # Convert the sentence to a list of characters
    # for in-place modification as strings are immutable in Python
    sentence = list(sentence)
    str_len = len(sentence) - 1

    # Reverse the whole sentence first
    str_rev(sentence, 0, str_len)
    start = 0

    # Iterate through the sentence to find and reverse each word
    for end in range(0, str_len + 1):
        if end == str_len or sentence[end] == ' ':
            # Include end character for the last word
            end_idx = end if end == str_len else end - 1
            # Reverse the current word
            str_rev(sentence, start, end_idx)
            # Move the "start" pointer to the start of the next word
            start = end + 1

    return ''.join(sentence)


def str_rev(_str, start_rev, end_rev):
    while start_rev < end_rev:
        _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
        start_rev += 1
        end_rev -= 1
