class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curMax = 1
        prev =  None
        count = 0
        for r in range(1, len(arr)):
            L = arr[r-1]
            R = arr[r]
            if prev == None:
                if L != R:
                    prev = L
                    count = 2
                    curMax = 2
            else:
                if prev < L and L > R:
                    count += 1
                elif prev > L and L < R:
                    count += 1
                else:
                    count = 2 if L != R else 1
                curMax = max(curMax, count)
                prev = L
        return curMax

                        