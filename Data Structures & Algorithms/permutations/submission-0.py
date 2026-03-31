class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []


        def backtrack(nums):
            if not nums:
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                perm.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:])
                perm.pop()
        
        backtrack(nums)
        return res