class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        curr = []
        i = 0

        def dfs(i):
            
            if i >= len(nums):
                subset.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)
        dfs(i)
        return subset
        