class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        output = 0


        for operation in operations:
            if operation not in ['+', 'D', 'C']:
                stack.append(int(operation))
                output += stack[-1]
            elif operation == '+':
                stack.append(stack[-1] + stack[-2])
                output += stack[-1]
            elif operation == 'D':
                stack.append(stack[-1] * 2)
                output += stack[-1]
            else:
                result = stack.pop()
                output -= result

        
        return output