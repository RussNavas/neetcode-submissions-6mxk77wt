class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = [0] * (2 * len(nums))

        for i in range(len(nums)):
            new[i] = nums[i]
        
        old = 0
        for i in range(len(nums), len(new)):
            new[i] = nums[old]
            old += 1
        return new