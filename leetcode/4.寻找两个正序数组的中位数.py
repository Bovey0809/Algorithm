#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = len(nums2) + len(nums1)
        if k % 2 == 0:
            # even
            return (first_k_element(k//2) + first_k_element(k//2 + 1)) // 2
        return first_k_element(k//2)

# @lc code=end
