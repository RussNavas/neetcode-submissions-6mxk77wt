class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        for r in range(ROWS):
            res = self.binarySearch(matrix[r], target)
            if res == True:
                return True
        return False

    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (r+l)//2
            if arr[m] == target:
                return True
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False