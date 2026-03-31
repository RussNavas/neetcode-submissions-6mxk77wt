class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights)-1

        while l < r:
            current_width = r - l
            current_area = min(heights[l], heights[r]) * current_width
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            elif heights[r] == heights[l]:
                l += 1
            maxA = max(maxA, current_area)
        return maxA



        