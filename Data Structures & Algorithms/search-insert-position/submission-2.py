class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        res = len(nums)
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:

                l = m + 1
            else:
                res = m
                r = m - 1
        return res