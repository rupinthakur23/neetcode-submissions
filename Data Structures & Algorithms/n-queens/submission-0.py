class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag, negDiag, col = set(), set(), set()
        result = []
        board = [['.'] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                col.add(c)
                negDiag.add(r -c)
                posDiag.add(r + c)
                board[r][c] = 'Q'
                backtracking(r + 1)
                col.remove(c)
                negDiag.remove(r -c)
                posDiag.remove(r + c)
                board[r][c] = '.'

        backtracking(0)
        return result