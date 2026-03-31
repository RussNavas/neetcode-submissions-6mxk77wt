class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.dfs(r, c, grid)
                    max_area = max(area, max_area)

        return max_area


    def in_bounds(self, r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def dfs(self, r, c, grid):
        if not self.in_bounds(r, c, grid) or grid[r][c] != 1:
            return 0

        grid[r][c] = 0

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        area = 1
        for d in dirs:
            area += self.dfs(r + d[0], c + d[1], grid)

        return area

        