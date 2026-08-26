class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for operation in tokens:
            if operation == '+':
                result.append(result.pop() + result.pop())
            elif operation == '-':
                a, b = result.pop(), result.pop()
                result.append(b - a)
            elif operation == '*':
                result.append(result.pop() * result.pop())
            elif operation == '/':
                a, b = result.pop(), result.pop()
                result.append(int(b/a))
            else:
                result.append(int(operation))
        
        return result[0]
            
        