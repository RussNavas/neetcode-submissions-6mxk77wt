class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for R in range(len(nums)):
            currentSum = max(currentSum, 0)
            currentSum += nums[R]
            maxSum = max(maxSum, currentSum)
        return maxSum