#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
# @lc code=start


class Solution:
    def compress(self, chars) -> int:
        read = write = anchor = 0
        while read < len(chars):
            if read + 1 != len(chars) and chars[read] == chars[read + 1]:
                read += 1
            else:
                digit = read - anchor + 1
                chars[write] = chars[anchor]
                write += 1
                anchor = read + 1
                if digit > 1:
                    for num in str(digit):
                        chars[write] = num
                        write += 1
                read += 1
        print(chars)
        return write
# @lc code=end


my = Solution()
# print(my.compress([""]))
print(my.compress(["a"]))
print(my.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(my.compress(["a", "b", "b", "b", "b",
                   "b", "b", "b", "b", "b", "b", "b", "b"]))
