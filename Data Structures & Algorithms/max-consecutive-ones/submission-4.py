class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                curr += 1
                maxCount = max(maxCount, curr)
            else:
                curr = 0
        return maxCount
    
        