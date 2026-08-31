class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c, prev):
            if (min(r, c) < 0 or r == ROWS or c == COLS or 
                matrix[r][c] <= prev):
                return 0
            if memo[r][c] != 0:
                return memo[r][c]
            
            path = 1
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                path = max(path, dfs(nr, nc, matrix[r][c]) + 1)
            memo[r][c] = path
            return path
        
        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c, float("-inf")))
        return max_path