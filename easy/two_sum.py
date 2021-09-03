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
