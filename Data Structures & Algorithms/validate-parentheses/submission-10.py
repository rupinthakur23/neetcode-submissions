class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = { '(': ')', '[': ']', '{': '}'}
        stack = []

        for elem in s:
            if elem in ['[', '{', '(']:
                stack.append(parenthesis[elem])
            else:
                if not stack or stack.pop() != elem:
                    return False
        return not stack
