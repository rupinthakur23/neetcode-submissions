class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])
        left , right = 0, (column * row) - 1

        while left <= right:
            mid = left + (right - left) // 2
            rowInd = mid // column
            colInd = mid  % column
            print(left)
            print(right)
            print(rowInd)
            print(colInd)
            print(mid)
            if matrix[rowInd][colInd] > target:
                right = mid -1
            elif matrix[rowInd][colInd] < target:
                left = mid + 1
            else:
                return True

        return False
        