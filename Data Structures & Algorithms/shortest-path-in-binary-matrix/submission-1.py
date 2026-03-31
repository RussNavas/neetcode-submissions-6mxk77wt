class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def bfs(x, y):
            ROWS, COLS = len(grid), len(grid[0])
            visited = set((x, y))
            q = deque([(x, y)])

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
                [1, 1],
                [-1, 1],
                [1, -1],
                [-1, -1]
            ]
            length = 1
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if(
                            nr < 0 or nc < 0 or
                            (nr, nc) in visited or
                            nr >= ROWS or
                            nc >= COLS or
                            grid[nr][nc] == 1
                        ):
                            continue

                        if nr == ROWS-1 and nc == COLS-1:
                            return length + 1

                        visited.add((nr, nc))
                        q.append((nr, nc))
                length += 1
            return -1

        res = bfs(0, 0)
        return res
