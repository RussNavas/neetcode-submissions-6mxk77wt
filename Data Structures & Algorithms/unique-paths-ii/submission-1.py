class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * (COLS) for r in range(ROWS)]
        def bfs(r, c, cache):
            if min(r, c) < 0 or r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            cache[r][c] = (bfs(r + 1, c, cache) + bfs(r, c + 1, cache))
            return cache[r][c]
        return bfs(0, 0, cache)