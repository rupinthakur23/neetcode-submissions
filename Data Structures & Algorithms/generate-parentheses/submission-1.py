class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtracking(openN, closedN):
            if openN == closedN == n:
                result.append(''.join(stack))
                return
            
            if closedN > openN:
                return
            
            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closedN)
                stack.pop()

            if closedN < n:
                stack.append(')')
                backtracking(openN, closedN + 1)
                stack.pop()
        
        backtracking(0, 0)
        return result