class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        top = 0
        bottom = row

        while(top <= bottom):
            mid = (top + bottom) // 2
            if( target < matrix[mid][0]):
                bottom = mid - 1
            elif (target > matrix[mid][-1]):
                top = mid + 1
            else:
                break
        
        if ( top > bottom): return False

         
        left = 0
        right = len(matrix[top]) -1
        row = (top + bottom) // 2


        while(left <= right):
            mid = (left + right) // 2
            if(target > matrix[row][mid]):
                left = mid + 1
            elif(target < matrix[row][mid]):
                right = mid - 1
            else:
                return True
        
        return False
        