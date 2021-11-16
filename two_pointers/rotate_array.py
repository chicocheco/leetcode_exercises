"""
https://leetcode.com/problems/rotate-array
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

from collections import deque


# brute force, my solution
# def rotate(nums, k):
#     for i in range(k):
#         nums.insert(0, nums.pop())


# deque
# def rotate(nums, k):
#     d = deque(nums)
#     d.rotate(k)
#     nums[:] = list(d)  # replace

# true 2-pointer solution (not mine)
def rotate(nums, k):
    def twopt(arr, i, j):
        """Swap elements at index i and j if j is greater than i."""
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
    if k > len(nums):
        k %= len(nums)
    if k > 0:
        twopt(nums, 0, len(nums) - 1)  # rotate entire array
        twopt(nums, 0, k - 1)  # rotate array up to k elements
        twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array


nums = [1, 4, 5, 7]
rotate(nums, 2)
print(nums)
