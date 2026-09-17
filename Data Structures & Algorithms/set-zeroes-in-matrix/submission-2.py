class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
             for row in range(ROWS):
                matrix[row][0] = 0
        
        if rowZero:
            for col in range(COLS):
                matrix[0][col] = 0
         