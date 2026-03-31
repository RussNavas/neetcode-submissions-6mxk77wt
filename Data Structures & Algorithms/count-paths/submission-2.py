class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        prevRow = [1] * n
        for r in range(m - 1):
            curRow = [1] * n
            for c in range(n-2, -1, -1):
                curRow[c] = prevRow[c] + curRow[c+1]
            prevRow = curRow
        return prevRow[0]