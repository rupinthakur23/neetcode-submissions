class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackDic = { '(':')', '[':']', '{':'}'}

        for elem in s:
            if elem in ['(', '[', '{']:
                stack.append(brackDic[elem])
            else:
                if not stack or stack.pop() != elem:
                    return False

        return not stack