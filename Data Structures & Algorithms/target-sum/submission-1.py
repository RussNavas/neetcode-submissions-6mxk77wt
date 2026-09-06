class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            memo[(i, curSum)] = ( backtrack(i + 1, curSum + nums[i]) + 
                                    backtrack(i + 1, curSum - nums[i]))
            return memo[(i, curSum)]
        return backtrack(0, 0)