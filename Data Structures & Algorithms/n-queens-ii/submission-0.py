class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag, negDiag, col = set(), set(), set()
        result = 0
        board = [[''] * n for i in range(n)]

        def backtracking(r):
            nonlocal result
            if r == n:
                result +=1
            
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                backtracking(r + 1)
                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)

        backtracking(0)
        return result
