class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            res = float('inf')
            for coin in coins:
                if coin <= amount:
                    res = min(1 + dfs(amount - coin), res)
            memo[amount] = res
            return memo[amount]
        
        soln = dfs(amount)
        return -1 if soln == float('inf') else soln 