class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curArea = dfs(r, c)
                    maxArea = max(maxArea, curArea)
        return maxArea
            