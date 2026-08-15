class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            if nums[l] <= nums[m]:
                # target is between l and m, go left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # else go right
                else:
                    l = m + 1
            # we are in the right sorted protion
            else:
                # target is between the mid point and the right, go right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # go left
                else:
                    r = m - 1 
        return -1