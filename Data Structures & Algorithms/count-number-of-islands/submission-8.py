class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if(
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == '0'):
                return 0

            grid[r][c] = '0'
            deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            island = 1
            for dr, dc in deltas:
                newr = r + dr
                newc = c + dc
                dfs(newr, newc)
            return island

        for r in range(ROWS):
            for c in range(COLS):
                islands += dfs(r, c)
        return islands
