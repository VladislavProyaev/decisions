from typing import List

url = "https://leetcode.com/problems/find-the-difference-of-two-arrays/description/"


class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)

        result_nums1 = [
            number for number in unique_nums1 if number not in unique_nums2
        ]
        result_nums2 = [
            number for number in unique_nums2 if number not in unique_nums1
        ]

        return [result_nums1, result_nums2]
