class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))

        for i in range(len(nums)):
            ans[i] = nums[i]
        j = 0
        for i in range(len(nums), len(ans)):
            ans[i] = nums[j]
            j += 1
        return ans
        