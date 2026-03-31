class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        # multi source bfs enque start points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        dirs = [[1, 0], [-1, 0], [0, 1], [0,-1]]
    
        # begin bfs
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        if fresh > 0:
            return -1
        return time

