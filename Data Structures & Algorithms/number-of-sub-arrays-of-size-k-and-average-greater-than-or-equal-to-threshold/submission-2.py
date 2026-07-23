class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k-1])
        count = 0

        for l in range(len(arr) - k + 1):
            total += arr[l + k - 1]
            avg = total / k
            if avg >= threshold:
                count += 1
            total -= arr[l]
        return count
        