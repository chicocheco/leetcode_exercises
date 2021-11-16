"""
https://leetcode.com/problems/search-insert-position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        curr = nums[pivot]
        if target == curr:
            return pivot
        if target < curr:
            right = pivot - 1
        else:
            left = pivot + 1
    return left  # no break and nothing returned in while loop


assert search_insert([7, 9, 11, 14], 14) == 3
assert search_insert([7, 9, 11, 14], 15) == 4
assert search_insert([7, 9, 11, 14], 8) == 1
assert search_insert([7, 9, 11, 14], 12) == 3


