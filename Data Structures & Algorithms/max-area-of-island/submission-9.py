class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1
            while q:
                r, c = q.popleft()
                
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if(min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0):
                            continue
                    
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area += 1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea
