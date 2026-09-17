class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        topLeft = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        topLeft = True

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        

        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0

        if topLeft:
            for col in range(COLS):
                matrix[0][col] = 0


            