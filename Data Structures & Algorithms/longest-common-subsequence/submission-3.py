class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        T: O(m * n)
        S: ()
        """
        ROWS, COLS = len(text1), len(text2)
        cache = [[-1]*COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            # cache hit
            if cache[r][c] != -1: 
                return cache[r][c]
            # mismatched chars so explore the cols of this row
            # and the rows of this column
            if text1[r] != text2[c]:
                cache[r][c] =  max(dfs(r, c + 1), dfs(r + 1, c))
            # match and no cache hit increment the count and move on the anti diag
            # this allows us to maintain char order and check a new char
            else:
                cache[r][c] = 1 + dfs(r + 1, c + 1)
            # return the answer
            return cache[r][c]
        return dfs(0, 0)