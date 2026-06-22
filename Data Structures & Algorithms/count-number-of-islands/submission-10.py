class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if ( min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                            grid[nr][nc] == '0'):
                            continue
                        q.append((nr, nc))
                        grid[nr][nc] = '0'
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += bfs(r, c)
        return islands
                
                        
