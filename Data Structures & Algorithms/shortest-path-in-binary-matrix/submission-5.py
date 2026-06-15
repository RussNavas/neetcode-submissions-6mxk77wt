class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        grid[0][0] = 1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if ( min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                        grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 1
            length += 1
        return -1

        