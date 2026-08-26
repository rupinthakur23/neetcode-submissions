class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in closeToOpen and stack:
                if closeToOpen[char] == stack[-1]:
                    stack.pop();
                else:
                    return False
            else:
                stack.append(char)
        return not stack

        