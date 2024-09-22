# Given an array, colors,
# which contains a combination of the following three elements:
# 0 (representing red)
# 1 (representing white)
# 2 (representing blue)
#
# Sort the array in place so that the elements of the same color are adjacent,
# with the colors in the order of red, white, and blue.
# To improve your problem-solving skills,
# do not utilize the built-in sort function.
#
# Constraints:
# 1 ≤ colors.length ≤ 300
# colors[i] can only contain 0, 1, or 2.
#
# Example 1:
# Input: [2, 1, 0, 1, 2, 0]
# Output: [0, 0, 1, 1, 2, 2]
#
# Example 2:
# Input: [2, 0, 1]
# Output: [0, 1, 2]


def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1

    # Iterate through the list until
    # the current pointer exceeds the end pointer
    while current <= end:
        if colors[current] == 0:
            # If the current element is 0,
            # swap it with the element at the start pointer
            colors[start], colors[current] = colors[current], colors[start]
            # Move both the start and current pointers one position forward
            current += 1
            start += 1

        elif colors[current] == 1:
            # If the current element is 1,
            # just move the current pointer one position forward
            current += 1

        else:
            # If the current element is 2,
            # swap it with the element at the end pointer
            colors[current], colors[end] = colors[end], colors[current]
            # Move the end pointer one position backward
            end -= 1
    return colors
