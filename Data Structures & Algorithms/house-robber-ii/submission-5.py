class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(arr[i] + dfs(i + 2, arr, memo), dfs(i + 1, arr, memo))
            return memo[i]
        return max(dfs(0, nums[:-1], {}), dfs(0, nums[1:], {}))