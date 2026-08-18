class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        curMax = float("-inf")
        for r in range(len(nums)):
            curMax = max(curMax, nums[r])
            if r - l + 1 < k:
                continue
            res.append(curMax)
            if curMax == nums[l]:
                curMax = float("-inf")
                for i in range(l + 1, r + 1):
                    curMax = max(curMax, nums[i])
            l += 1
        return res