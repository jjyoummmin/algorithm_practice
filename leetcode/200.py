# 2D array DFS
class Solution:
    def numIslands(self, grid) -> int:
        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        h, w = len(grid), len(grid[0])
        
        def dfs(x, y):
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    dfs(nx, ny)
            
        num_islands = 0 
        for x, row in enumerate(grid):
            for y, point in enumerate(row):
                if point != '1':
                    continue
                num_islands += 1
                dfs(x, y)

        return num_islands