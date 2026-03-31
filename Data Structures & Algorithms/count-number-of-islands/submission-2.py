class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        coords = [(-1,0), (1,0), (0,-1), (0,1)]

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        

        def in_bounds(r, c):
            return (0 <= r < rows) and (0<= c < cols)

        def dfs(r,c):

            if not in_bounds(r,c) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            for dr, dc in coords:
                dfs(r + dr, c +dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands


        
        