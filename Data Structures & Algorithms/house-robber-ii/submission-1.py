class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        r1, r2 = 0,0

        for num in nums:
            temp = max(r1 + num, r2)
            r1 = r2
            r2 = temp

        return r2
        