class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for value in tokens:
            if value not in ['+', '-', '*', '/']:
                stack.append(int(value))
            else:
                if value == '+':
                    stack.append(stack.pop() + stack.pop())
                elif value == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif value == '*':
                    stack.append(stack.pop() * stack.pop())
                elif value == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
        return stack[0]
                
