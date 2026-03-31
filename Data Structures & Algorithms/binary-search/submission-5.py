class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums)-1
        while L <= R:
            mid = (L + R) // 2
            val = nums[mid]
            if target < val: # move left
                R = mid - 1
            elif target > val: # move right
                L = mid + 1
            else:
                return mid
        return -1
        