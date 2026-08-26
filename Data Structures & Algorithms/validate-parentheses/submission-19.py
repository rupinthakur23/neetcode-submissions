class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        combinations = {"(" : ")", "[":"]", "{" : "}"}

        for index, value in enumerate(s):
            if value in combinations:
                stack.append(value)
            else:
                if stack and combinations[stack[-1]] == value:
                    stack.pop()
                else:
                    return False 
     
        return len(stack) == 0 


