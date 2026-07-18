class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        total = 0
        for num in nums:
            total = max(total, 0)
            total += num
            maxSum = max(maxSum, total)
        return maxSum