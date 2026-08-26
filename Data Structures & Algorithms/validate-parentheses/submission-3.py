class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if (len(s) % 2) != 0:
             return False
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if(len(stack)>0 and stack[-1] == '(' and char == ')' ):
                    stack.pop()
                    continue
                elif(len(stack)>0 and stack[-1] == '[' and char == ']' ):
                    stack.pop()
                    continue
                elif(len(stack)>0 and stack[-1] == '{' and char == '}' ):
                    stack.pop()
                    continue
                return False
        return not stack