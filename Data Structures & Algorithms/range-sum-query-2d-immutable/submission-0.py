class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.result = []
        for row in range(len(matrix)):
            target = 0
            window = []
            for col in range(len(matrix[0])):
                target += matrix[row][col]
                window.append(target)
            self.result.append(window)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.result[row][col2] - self.result[row][col1 - 1]
            else:
                res += self.result[row][col2]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)