from typing import List

url = "https://leetcode.com/problems/rotate-function/description/"


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        nums_length = len(nums)
        total_sum = sum(nums)
        current_sum = sum(i * nums[i] for i in range(nums_length))
        result = current_sum
        for i in range(1, nums_length):
            current_sum += total_sum - nums_length * nums[nums_length - i]
            result = max(result, current_sum)
        return result
