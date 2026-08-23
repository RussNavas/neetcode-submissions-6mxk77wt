class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(coins, amount, memo):
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            min_coins = float('inf')
            for coin in coins:
                if coin <= amount:
                    min_coins = min(min_coins, 1 + dfs(coins, amount - coin, memo))
            memo[amount] = min_coins
            return memo[amount]
        
        res = dfs(coins, amount, memo)
        return -1 if res == float('inf') else res