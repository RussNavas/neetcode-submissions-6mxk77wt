class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2 * len(nums))
        a = 0
        for i in range(len(nums)):
            ans[a] = nums[i]
            a += 1
        for i in range(len(nums)):
            ans[a] = nums[i]
            a += 1
        return ans