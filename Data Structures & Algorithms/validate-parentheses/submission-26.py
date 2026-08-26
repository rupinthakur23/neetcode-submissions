class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {'}' :'{', ']':'[', ')':'('}
        stack = []

        for char in s:
            if char not in bracketMap:
                stack.append(char)
            else:
                if not stack or stack.pop() != bracketMap[char]:
                    return False
        
        return True if len(stack) == 0 else False