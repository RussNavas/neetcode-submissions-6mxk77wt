class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        if not nums:
            return []

        def dfs(i):

            if i == len(nums) and sum(cur) == target:
                res.append(cur[:])
                return

            if sum(cur) > target or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(i)
            cur.pop()
            dfs(i+1)
            return
        dfs(0)
        return res