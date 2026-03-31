class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # non decreasing i.e. there are dups
        # remove dups in place
        # return the num of unique elements
        # two pointers, one for ref and one to search using
        # a two idx wide window to scan for boundaries

        l = 1 # start at 1 since 0th idx is always valid
        
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l