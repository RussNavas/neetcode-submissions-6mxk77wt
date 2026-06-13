class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0):
                return 0
            
            
            grid[r][c] = 0
            deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            area = 1
            for dr, dc in deltas:
                newr = r + dr
                newc = c + dc
                area += dfs(newr, newc)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                maxarea = max(maxarea, dfs(r, c))
        return maxarea
