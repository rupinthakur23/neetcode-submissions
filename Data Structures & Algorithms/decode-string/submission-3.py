class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                value1 = ''
                value2 = ''
                while stack and stack[-1] != '[':
                    value1 = stack.pop() + value1
                
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    value2 = stack.pop() + value2
                
                stack.append(int(value2) * value1)
            else:
                stack.append(char)
                    
        return ''.join(stack)
