"""
https://leetcode.com/problems/binary-search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

"""
Algorithm
    Initialise left and right pointers : left = 0, right = n - 1.
    While left <= right :
        Compare middle element of the array nums[pivot] to the target value target.
            If the middle element is the target target = nums[pivot] : return pivot.
            If the target is not yet found :
                If target < nums[pivot], continue the search on the left 
                    right = pivot - 1.
                Else 
                    continue the search on the right left = pivot + 1
"""


def search(nums, target):
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
    return -1


assert search([7, 9, 11, 14], 14) == 3
assert search([7, 9, 11, 14], 15) == -1
assert search([7, 9, 11, 14], 8) == -1
assert search([7, 9, 11, 14], 12) == -1
