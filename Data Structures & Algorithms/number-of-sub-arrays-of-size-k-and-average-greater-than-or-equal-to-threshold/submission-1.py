class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window = []
        l = 0
        count = 0
        for r in range(len(arr)):
            if (r - l + 1 ) > k:
                window = window[1:]
                l += 1
            window.append(arr[r])

            if  len(window) == k:
                avg = sum(window) / len(window)
                if avg >= threshold:
                    count += 1

        return count