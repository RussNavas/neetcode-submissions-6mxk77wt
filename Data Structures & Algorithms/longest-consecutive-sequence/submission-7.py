class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxLen = 0

        for num in nums:
            # check if start of sequence
            if (num - 1) not in hashSet:
                length = 0
                while (num + length) in hashSet:
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen
