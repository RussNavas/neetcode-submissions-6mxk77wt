class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = 0
        for n in nums:
            if n - 1 not in numSet:
                curSeq = 1
                maxSeq = max(maxSeq, curSeq)
                curNum = n
                while curNum + 1 in numSet:
                    curSeq += 1
                    maxSeq = max(maxSeq, curSeq)
                    curNum += 1
        return maxSeq 