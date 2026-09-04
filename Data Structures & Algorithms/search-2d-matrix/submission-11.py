class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS -1

        while left <= right:
            mid = left + (right - left)//2
            midValue = matrix[mid // COLS][mid % COLS]

            if midValue > target:
                right = mid - 1
            elif midValue < target:
                left = mid + 1
            else:
                return True
        
        return False

            