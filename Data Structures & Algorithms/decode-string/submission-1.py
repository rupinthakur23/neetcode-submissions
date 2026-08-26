class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                outputString = ""
                while(stack[-1] != "["):
                    outputString = stack.pop() + outputString
                
                stack.pop()
                
                counter = ""
                while(stack and stack[-1].isdigit()):
                    counter = stack.pop() + counter
                
                stack.append(int(counter) * outputString)
        
        return "".join(stack)