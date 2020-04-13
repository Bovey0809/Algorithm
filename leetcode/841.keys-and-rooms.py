#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(key):
            for room in rooms[key]:
                if room in visited:
                    continue
                else:
                    visited.append(room)
                    dfs(room)        
        visited = [0]
        dfs(0)
        return len(visited) == len(rooms)
# @lc code=end

