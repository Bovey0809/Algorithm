# @lc app=leetcode id=46 lang=python3
# @lc code=start

class Solution:
    def permute(self, nums:list) -> list:
        if len(nums) == 1:
            return [nums]
        output = []
        for num in nums:
            index = nums.index(num)
            for perm in self.permute(nums[:index] + nums[index + 1 :]):
                output.append(perm + [num])
        return output
                
# @lc code=end

me = Solution()
print(me.permute([1, 2, 3]))
print(me.permute([1]))

