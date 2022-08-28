# 2D array DFS
class Solution:
    def floodFill(self, image, sr, sc, color):
        h, w = len(image[0]), len(image)
        initial_color = image[sr][sc]
        def dfs(x, y):
            image[x][y] = color
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y+ dy
                if 0 <= nx < w and 0 <= ny < h and image[nx][ny] == initial_color:
                    dfs(nx, ny)
        
        if initial_color != color:
            dfs(sr, sc)

        return image