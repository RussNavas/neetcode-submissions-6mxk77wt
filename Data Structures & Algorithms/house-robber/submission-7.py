class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            # max of taking the house or not taking the house
            cache[i] = max(dfs(i+1, cache), nums[i] + dfs(i+2, cache))
            return cache[i]
        return dfs(0, {})