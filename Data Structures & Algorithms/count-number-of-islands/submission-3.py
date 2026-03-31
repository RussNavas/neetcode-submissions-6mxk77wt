class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0
        def dfs(r, c):

            if ((min(r, c) < 0) or 
                (r >= ROWS or c >= COLS) or
                (grid[r][c] == '0')):
                return

            grid[r][c] = '0'

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count
        