#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
# @lc code=start


class Solution:
    def compress(self, chars) -> int:

        # @lc code=end


my = Solution()
# print(my.compress([""]))
print(my.compress(["a"]))
print(my.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(my.compress(["a", "b", "b", "b", "b",
                   "b", "b", "b", "b", "b", "b", "b", "b"]))
