class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxSeq = 0
        curSeq = 1
        for num in nums:
            if num - 1 not in hashSet:
                # valid start
                n = num
                while n + 1 in hashSet:
                    curSeq += 1
                    n += 1
                maxSeq = max(curSeq, maxSeq)
                curSeq = 1

        return maxSeq

                    
