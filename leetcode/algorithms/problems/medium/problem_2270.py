from typing import List

url = "https://leetcode.com/problems/number-of-ways-to-split-array/description/"


class Solution:
    def waysToSplitArray(self, nums_: List[int]) -> int:
        result = 0
        total_sum = sum(nums_)
        left_sum = 0
        for i in range(len(nums_) - 1):
            left_sum += nums_[i]
            right_sum = total_sum - left_sum

            if left_sum >= right_sum:
                result += 1

        return result
