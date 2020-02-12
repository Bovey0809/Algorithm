#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
# @lc code=start


class Solution:
    def compress(self, chars) -> int:
        write = read = anchor = 0
        for read in range(len(chars)):
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]
                write += 1
                count = read - anchor + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
# @lc code=end


my = Solution()
# print(my.compress([""]))
print(my.compress(["a"]))
print(my.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(my.compress(["a", "b", "b", "b", "b",
                   "b", "b", "b", "b", "b", "b", "b", "b"]))
