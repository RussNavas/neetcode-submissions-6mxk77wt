class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        circular array, cannot rob adj hosues i.e. no nums[1] & nums[-1]
        max with subproblems => dp

        consider that we can just cut off the 1st and last houses  and
        do two dfs returning the max of those explorations overall
        """
        if len(nums) == 1:
            return nums[0]
        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2, nums, memo), dfs(i + 1, nums, memo))
            return memo[i]
        
        return max(dfs(0, nums[1:], {}), dfs(0, nums[:-1], {}))