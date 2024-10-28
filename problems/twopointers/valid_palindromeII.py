def is_palindromeII(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_pal(s, left + 1, right) or is_pal(s, left, right - 1)
    return True


def is_pal(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
