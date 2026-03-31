class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and
                        0 <= col < COLS and
                        grid[row][col] == 1):

                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1