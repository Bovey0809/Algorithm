#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        paths = []

        def backtracing(nums, depth, path):
            if depth == length:
                paths.append(copy.deepcopy(path))
            while nums:
                prev = path[-1]
                num = nums.pop(0)
                if num == prev:
                    continue
                else:
                    path.append(num)
                    backtracing(nums, depth+1, path)
                    path.pop()
        backtracing(nums, 0, [nums[0]])
        return paths
# @lc code=end
