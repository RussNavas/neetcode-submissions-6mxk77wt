class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        
        q = deque()
        q.append((0, 0))
        visited = set()

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        pathLen = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return pathLen + 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if(min(nr, nc) < 0 or nr == ROWS or nc == COLS 
                        or (nr, nc) in visited or grid[nr][nc] == 1):
                        continue
                    
                    visited.add((nr, nc))
                    q.append((nr, nc))
            pathLen += 1
        return -1
