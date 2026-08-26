class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracketMap[bracket]:
                    return False
        
        return True if not stack else False

        