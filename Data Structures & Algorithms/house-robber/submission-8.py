class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(n):
            if n >= len(nums):
                return 0
            if n in cache:
                return cache[n]
            
            cache[n] = max(dfs(n + 1), nums[n] + dfs(n + 2))
            return cache[n]
        return dfs(0)