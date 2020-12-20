#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(first=0):
            if first == n:
                res.append(nums[:])  # why
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrace(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrace()
        print(res)
        return res


# @lc code=end
me = Solution()
me.permute([1, 2])
