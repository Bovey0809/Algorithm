# @lc app=leetcode id=46 lang=python3
# @lc code=start


class Solution:
    def permute(self, nums: list) -> list:
        # Base Case
        if len(nums) == 1:
            return [nums]
        result = []
        for num in nums:
            index = nums.index(num)
            for perm in self.permute(nums[:index] + nums[index + 1 :]):
                result.append([num]+perm)
        return result

# @lc code=end


me = Solution()
print(me.permute([1, 2, 3]))
print(me.permute([1]))
