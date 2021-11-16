"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""


# my slow solution:
# def move_zeroes(nums: list):
#     count = nums.count(0)
#     for i, v in enumerate(nums):
#         if v == 0:
#             del nums[i]
#     for i in range(count):
#         nums.append(0)
#
#
# nums = [0, 6, 1, 3, 0, 5]
# move_zeroes(nums)
# assert nums == [6, 1, 3, 5, 0, 0]


# someone else's faster solution:
def move_zeroes(nums: list):
    """
    If the current element is not 0 but the previous one was, swap them so the 0 is shifted to the right.
    This assures to preserve other elements at the same indexes.
    """
    slow = 0  # index where to shift a non-zero element
    for i, v in enumerate(nums):
        if v != 0 and nums[slow] == 0:  # pointer 1 and pointer 2
            nums[slow], nums[i] = v, nums[slow]  # swap
        if nums[slow] != 0:
            slow += 1  # shift pointer 2


nums = [0, 6, 1, 3, 0, 0, 5]
move_zeroes(nums)
print(nums)
