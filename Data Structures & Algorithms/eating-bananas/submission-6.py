class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = float('inf')
        piles.sort()
        low = 1
        high = max(piles)
        while low <= high:
            mid = (high + low) // 2
            rate = mid
            timeTaken = self.rateTest(piles, rate)
            if timeTaken <= h:
                minRate = min(minRate, rate)
                high = mid - 1
            else:
                low = mid + 1
        return minRate

    def rateTest(self, piles, rate):
        timeTaken = 0
        for p in piles:
            timeTaken += (-(p // -rate))
        return timeTaken
        

    

