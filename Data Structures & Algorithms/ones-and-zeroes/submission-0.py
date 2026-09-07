class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in memo:
                return memo[(i, m, n)]
            zeros, ones = strs[i].count("0"), strs[i].count("1")
            memo[(i, m, n)] = dfs(i + 1, m, n)
            if zeros <= m and ones <= n:
                memo[(i, m, n)] = max(
                    memo[(i, m, n)],  
                   1 + dfs(i + 1, m - zeros, n - ones)
                )
      
            return memo[(i, m, n)]
        return dfs(0, m, n)