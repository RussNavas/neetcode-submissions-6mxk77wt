class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i == len(days):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = float("inf")
            j = i
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                memo[i] = min(memo[i], cost + dfs(j))
            return memo[i]

        return dfs(0)