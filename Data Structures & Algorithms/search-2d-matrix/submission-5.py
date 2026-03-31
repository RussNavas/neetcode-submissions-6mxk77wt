class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for row in range(len(matrix)):
            l,r = 0, len(matrix[0])-1
            while l <= r:
                mid = (r + l) // 2
                val = matrix[row][mid]
                if target < val:
                    r = mid - 1
                elif target > val:
                    l = mid + 1
                else:
                    return True
            l,r = 0, len(matrix[0])-1
        return False

            