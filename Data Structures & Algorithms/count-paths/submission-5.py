class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]*n for r in range(m)]

        def bfs(r, c, cache):
            if r == m - 1 and c == n - 1:
                return 1
            if r == m or c == n:
                return 0
            if cache[r][c] != 0:
                return cache[r][c]

            cache[r][c] = (bfs(r + 1, c, cache) + bfs(r, c+1, cache))
            return cache[r][c]
        
        
        return bfs(0, 0, cache)