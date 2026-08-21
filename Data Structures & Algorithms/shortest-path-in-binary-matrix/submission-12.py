class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        q = deque()
        visited = set()
        q.append((0, 0))

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r, c) in visited:
                    continue
                if r == ROWS -1 and c == COLS - 1:
                    return length + 1
                visited.add((r, c))
                for dr, dc in dirs:
                    q.append((r + dr, c + dc))
            length += 1
        return -1

            
