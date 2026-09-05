class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                operand = ''
                operator = ""

                while stack and stack[-1] != '[':
                    operand = stack.pop() + operand
                stack.pop()
                while stack and stack[-1].isdigit():
                    operator = stack.pop() + operator
                stack.append(int(operator) * operand)
            else:
                stack.append(char)
        
        return ''.join(stack)