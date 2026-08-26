class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split('/')
        stack = []
        
        for char in words: 
            if char == "..":
                if stack:
                    stack.pop()
            elif char != "" and char !='.':
                stack.append(char)
                    
        result = "/" + "/".join(stack)
        return result
            