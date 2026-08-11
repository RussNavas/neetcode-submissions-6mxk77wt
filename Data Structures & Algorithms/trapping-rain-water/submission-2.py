class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxLeft, maxRight, = height[0], height[-1]
        l, r = 0, len(height)

        count = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                count += maxLeft - height[l]

            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                count += maxRight - height[r]
        return count
            
            