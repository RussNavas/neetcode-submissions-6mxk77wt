class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        fruit = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fruit += 1

        while fruit > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fruit -= 1
            time += 1
        if fruit == 0:
            return time
        return -1
