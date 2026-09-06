class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
    
    def lcs(self, s1, s2):
        ROWS, COLS = len(s1), len(s2)
        dp = [ [0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if s1[r] == s2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r][c + 1], dp[r + 1][c])
        return dp[0][0]