class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums)-1
        while l < r:
            m = r - l // 2
            if nums[m] < res:
                res = nums[m]

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
