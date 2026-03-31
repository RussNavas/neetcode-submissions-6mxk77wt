class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        coords = [(-1,0), (1,0), (0,-1), (0,1)]

        island = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def in_bounds(r, c, grid):
            return (
                (0 <= r < ROWS) 
                        and (0 <= c < COLS)
                        )

        def dfs(r, c):
            if not in_bounds(r, c, grid) or grid[r][c] == '0':
                return

            grid[r][c] = "0" # flip the value to prevent double counts
            for dr, dc in coords:
                dfs(r + dr, c + dc)

            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1

        return island


        



        