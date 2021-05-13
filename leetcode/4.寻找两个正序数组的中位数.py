#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_k_element(nums1, nums2, k):
            # base condition
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1
            # empty
            if not nums1:
                return nums2[k-1]
            # k == 1
            if k == 1:
                return min(nums1[0], nums2[0])
            # out of range
            t = min(k//2, len(nums1))
            if nums1[t-1] < nums2[t-1]:
                return find_k_element(nums1[t:], nums2, k-t)
            else:
                return find_k_element(nums1, nums2[t:], k-t)

        k = len(nums2) + len(nums1)

        if k % 2 == 0:
            # even
            return (find_k_element(nums1, nums2, k//2+1) + find_k_element(nums1, nums2, k//2)) / 2
        return find_k_element(nums1, nums2, (k + 1)//2)


# @lc code=end
me = Solution()
print(me.findMedianSortedArrays([1, 3], [2, 4]))
