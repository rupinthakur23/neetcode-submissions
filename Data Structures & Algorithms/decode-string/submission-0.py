class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                output = ""
                while stack[-1] != '[':
                    output = stack.pop() + output
                stack.pop() 

                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                
                stack.append(int(count) * output)
        return "".join(stack)

