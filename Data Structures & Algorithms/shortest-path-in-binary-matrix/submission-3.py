class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                dirs = [[0,1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
                for dr, dc in dirs:
                    newr = r + dr
                    newc = c + dc
                    if(min(newr, newc) < 0 or
                        newr == ROWS or newc == COLS or
                        (newr, newc) in visited or
                        grid[newr][newc] == 1):
                        continue
                    queue.append((newr, newc))
                    visited.add((newr, newc))
            length += 1
        return -1