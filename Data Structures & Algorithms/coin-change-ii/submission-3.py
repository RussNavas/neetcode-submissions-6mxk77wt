class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, cur_amount):
            if i == len(coins) or cur_amount > amount:
                return 0
            if cur_amount == amount:
                return 1
            if (i, cur_amount) in cache:
                return cache[(i, cur_amount)]
            
            cache[(i, cur_amount)] = dfs(i, cur_amount + coins[i]) + dfs(i + 1, cur_amount)
            return cache[(i, cur_amount)]
        return dfs(0, 0)