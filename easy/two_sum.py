"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Runtime: 9278 ms, faster than 5.00% of Python3 online submissions for Two Sum.
Memory Usage: 14.6 MB, less than 98.27% of Python3 online submissions for Two Sum.
"""


def two_sum(nums, target):
    """find non-identical indexes"""

    for i, j in enumerate(nums):
        for k, l in enumerate(nums):
            summ = j + l
            if summ == target:
                if i == k:
                    continue
                else:
                    return [i, k]


print(two_sum([3, 2, 3], 6))
