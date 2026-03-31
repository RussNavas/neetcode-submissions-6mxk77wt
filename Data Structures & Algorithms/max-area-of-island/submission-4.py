class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area



        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curArea = bfs(r, c)
                    maxArea = max(maxArea, curArea)
        return maxArea
            