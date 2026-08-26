class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for value in tokens:
            if value not in ['+', '-', '*', '/' ]:
                stack.append(value)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if value == '+':
                    stack.append(a + b)
                elif value == '-':
                    stack.append(a - b)
                elif value == '*':
                    print(a)
                    print(b)
                    stack.append(a * b)
                elif value == '/':
                    stack.append(int(a / b))
        return int(stack[0])