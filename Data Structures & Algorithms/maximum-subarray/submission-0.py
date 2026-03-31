class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # subaarray must be contiguous by definition

        maxSum = nums[0] # arbitrary
        currSum = 0 # counter

        for num in nums:
            # check if adding this value is worth it, otherwise move on
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)
        return maxSum
        