class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return
            backtrack(path, idx + 1)
            path.append(nums[idx])
            backtrack(path, idx + 1)
            path.pop()

        backtrack([], 0)
        return res