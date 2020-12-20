#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = set()
        opened.add(0)
        def dfs(room:int, opened:set):
            for key in rooms[room]:
                if key not in opened:
                    opened.add(key)
                    dfs(key, opened)
        
        dfs(0, opened)
        return len(opened) == len(rooms)
# @lc code=end

