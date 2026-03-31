class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minimum = float("inf")
        total = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minimum = min(minimum, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if minimum == float("inf") else minimum
