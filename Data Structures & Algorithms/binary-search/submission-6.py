class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (r + l) // 2
            val = nums[mid]
            if target < val:
                r = mid - 1
            elif target > val:
                l = mid + 1
            else:
                return mid
        return -1
        