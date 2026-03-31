class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []
        i = 0
        nums.sort()

        def dfs(i, nums, curr, subsets):
            if i == len(nums):
                subsets.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1, nums, curr, subsets)
            curr.pop()

            # skip dups
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1, nums, curr, subsets)

        dfs(i, nums, curr, subsets)
        return subsets
        