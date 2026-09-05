class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        nums is an array of houses
        nums[i] is money
        allowed movment is 
            i + i + 2 or i + 1 i.e.
            take the house skip its neighbor 
            or start from the neighbor
        max greedy problem therefore dp
        """

        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        return dfs(0)