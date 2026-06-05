class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        total = 0
        def dfs(i):
            nonlocal total
            if total == target:
                res.append(cur[:])
                return
            if i == len(nums) or total > target:
                return
            total += nums[i]
            cur.append(nums[i])
            dfs(i)
            total -= nums[i]
            cur.pop()
            dfs(i+1)
            return
        dfs(0)
        return res