class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        ans = [0] * n
        for i in range(n-1, -1, -1):
            ans[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return ans