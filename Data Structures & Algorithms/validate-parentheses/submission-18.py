class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        combinations = {"(" : ")", "[":"]", "{" : "}"}

        for index, value in enumerate(s):
            if value in combinations:
                stack.append(value)
            else:
                if not stack or combinations[stack.pop()]!= value:
                    return False 
     
        return len(stack) == 0 


