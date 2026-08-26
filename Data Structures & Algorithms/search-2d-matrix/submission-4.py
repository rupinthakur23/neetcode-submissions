class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        top = 0
        bottom = rows

        while(top <= bottom):
            mid = (top + bottom)//2

            if(target > matrix[mid][-1]):
                top = mid + 1
            elif(target < matrix[mid][0]):
                bottom = mid - 1
            else:
                break
        
        if (top > bottom): return False

        row = (top + bottom)//2

        left , right = 0, cols

        while(left <= right):
            mid = (left + right)//2
            if(target > matrix[row][mid]):
                left = mid + 1
            elif(target < matrix[row][mid]):
                right = mid - 1
            else:
                return True
        
        return False


