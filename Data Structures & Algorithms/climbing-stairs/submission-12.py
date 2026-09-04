class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i < 1:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in cache:
                return cache[i]
            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]
        return dfs(n)