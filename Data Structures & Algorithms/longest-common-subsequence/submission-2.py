class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        cache = [[0]*COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if cache[r][c]: 
                return cache[r][c]
            if text1[r] != text2[c]:
                cache[r][c] +=  max(dfs(r, c + 1), dfs(r + 1, c))

            else:
                cache[r][c] = 1 + dfs(r + 1, c + 1)
            return cache[r][c]
        return dfs(0, 0)