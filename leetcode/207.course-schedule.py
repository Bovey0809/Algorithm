#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # It's a top sort.
        # make a graph
        graph = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        course_status = [0] * numCourses

        # dfs
        def dfs(course):
            if course_status[course] == 1:
                return True
            elif course_status[course] == -1:
                return False
            course_status[course] = -1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            course_status[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


# @lc code=end
me = Solution()
print(me.canFinish(2, [[1, 0], [0, 1]]))
