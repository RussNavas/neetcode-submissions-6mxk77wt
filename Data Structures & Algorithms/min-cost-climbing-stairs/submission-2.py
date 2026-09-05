class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        cost is a list of tolls
        can step by i + 1 or i + 2
        can start at 0 or 1 so need two dfs calls
        min => greedy
        traveral ends at i == len(cost)
        """

        def dfs(i, memo):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(cost[i] + dfs(i + 2, memo), dfs(i + 1, memo) + cost[i])
            return memo[i]
        
        return min(dfs(0, {}), dfs(1, {}))