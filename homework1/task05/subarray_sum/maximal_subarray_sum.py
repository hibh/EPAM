"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k:
        print("Sum of all elements")
        return sum(nums)
    if type(k) not in [int]:
        raise TypeError("a must be integer")
    total = 0
    for i in range(k):
        total += nums[i]

    current_sum = total
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        total = max(total, current_sum)

    return total
