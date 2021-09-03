"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Runtime: 73 ms, faster than 5.63% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.1 MB, less than 90.83% of Python3 online submissions for Reverse Integer.
"""

_MIN = -2 ** 31
_MAX = 2 ** 31 - 1


def reverse(x):
    """reverse the number as string"""

    str_digit = str(abs(x))
    str_rev = str_digit[::-1]

    if x < 0:
        rev = int(str_rev) * -1
    else:
        rev = int(str_rev)
    if not _MIN < rev < _MAX:
        return 0
    return rev


print(reverse(-123))
print(reverse(1534236469))
