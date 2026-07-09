class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        minSum = nums[0]
        maxSum = nums[0]

        curSum = 0
        for num in nums:
            curSum = min(curSum, 0)
            curSum += num
            minSum = min(minSum, curSum)

        curSum = 0
        for num in nums:
            curSum = max(curSum, 0)
            curSum += num
            maxSum = max(maxSum, curSum)

        return max(maxSum, sum(nums) - minSum) if maxSum > 0 else maxSum
        
        