#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        xRange = len(grid[0])
        yRange = len(grid)
        count = 0
        
        def dfs(y, x):
            grid[y][x] = '0'
            nextMove = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for xMove, yMove in nextMove:
                next_x, next_y = x + xMove, y + yMove 
                if not (0 <= next_x < xRange and 0 <= next_y < yRange):
                    continue
                if grid[next_y][next_x] == '1':
                    grid[next_y][next_x] == '0'
                    dfs(next_y, next_x)

        for x in range(xRange):
            for y in range(yRange):
                if grid[y][x] == '1':
                    count += 1
                    dfs(y, x)
        
        return count
# @lc code=end

