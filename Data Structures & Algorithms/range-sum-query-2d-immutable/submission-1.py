class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrixPrefix = []
        for row in range(len(matrix)):
            subPrefix = []
            total = 0
            for col in range(len(matrix[0])):
                total += matrix[row][col]
                subPrefix.append(total)
            self.matrixPrefix.append(subPrefix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for row in range(row1, row2 +1):

            leftIndex = self.matrixPrefix[row][col1 -1] if col1 - 1 >= 0 else 0
            result += self.matrixPrefix[row][col2] - leftIndex

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)