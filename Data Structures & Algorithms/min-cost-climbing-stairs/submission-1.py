class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = min(dfs(i + 1) + cost[i], dfs(i + 2) + cost[i])
            return memo[i]
        return min(dfs(0), dfs(1))