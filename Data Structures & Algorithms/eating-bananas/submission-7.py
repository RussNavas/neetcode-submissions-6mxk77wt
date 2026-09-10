class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k = b / hr implies hr = b/k
        """
        piles.sort()
        l = 1
        r = piles[-1]
        res = r
        while l <= r:
            rate = ( r + l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            if time <= h:
                r = rate - 1
                res = rate
            else:
                l = rate + 1
        return res
