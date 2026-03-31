class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        curr = []
        i = 0

        def dfs(i, nums, curr, subset):
            
            if i >= len(nums):
                subset.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1, nums, curr, subset)

            curr.pop()
            dfs(i+1, nums, curr, subset)
        dfs(i, nums, curr, subset)
        return subset
        