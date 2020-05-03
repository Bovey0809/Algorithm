#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_status = [False] * len(rooms)
        stack = [0]
        while stack:
            room = stack.pop()
            rooms_status[room] = True
            for key in rooms[room]:
                if not rooms_status[key]:
                    stack.append(key)
        return all(rooms_status)

# @lc code=end

