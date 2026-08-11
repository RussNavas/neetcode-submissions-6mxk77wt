class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxArea = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            area = width * height

            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea

