class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {"}" : "{", ")" : "(", "]" : "["}

        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracketMap[bracket]:
                    return False
        
        return len(stack) == 0