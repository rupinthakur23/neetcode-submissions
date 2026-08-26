class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for value in operations:
            if value not in ['+', 'C', 'D']:
                stack.append(int(value))
            else:
                if value == '+':
                    stack.append(stack[-1] + stack[-2])  
                elif value == 'C':
                    stack.pop()
                elif value == 'D':
                    stack.append(stack[-1] * 2)  
        return sum(stack)
        