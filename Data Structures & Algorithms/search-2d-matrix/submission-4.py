class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        # find a suitable row 
        target_row = 0
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break

            elif matrix[mid][0] > target:
                r = mid - 1

            else:
                l = mid + 1
        else:
            return False # taget not in any row range

        # search row
        l = 0
        r = len(matrix[target_row])-1

        while l <= r:
            mid = (l + r) // 2

            if matrix[target_row][mid] == target:
                return True

            elif matrix[target_row][mid] < target:
                l = mid + 1

            elif matrix[target_row][mid] > target:
                r = mid - 1

        return False
        