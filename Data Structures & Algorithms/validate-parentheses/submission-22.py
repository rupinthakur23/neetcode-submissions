class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {'}' : "{", "]" : "[", ")" : "("}
        stack = []

        for char in s:
            if char not in parenthesesMap:
                stack.append(char)
            else:
                if not stack or stack.pop() != parenthesesMap[char]:
                    return False
        
        return True if len(stack) == 0 else False