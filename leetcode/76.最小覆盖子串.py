#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
import collections
# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 从right开始, 维护两个字典, 一个 win_freq, 一个 need
        need = collections.Counter(t)
        left = right = 0
        minimum = len(s) + 1
        distance = 0  # distance 代表窗口内的包含的t中的元素的个数.
        res = s[left:right]
        while right < len(s):
            # 处理 right 的逻辑
            if s[right] in need:
                if need[s[right]] > 0:  # 说明当前位置的right是需要的.
                    distance += 1
                need[s[right]] -= 1

            # 当所有的元素都已经包含进去的时候, 处理left的逻辑
            while distance == len(t):
                if right - left < minimum:
                    minimum = right - left
                    res = s[left:right+1]
                if s[left] in need:
                    if need[s[left]] == 0:
                        distance -= 1
                    need[s[left]] += 1
                left += 1
            right += 1
        return res


# @lc code=end


s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
me = Solution()
print(me.minWindow(s, t))
