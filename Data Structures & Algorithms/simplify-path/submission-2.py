class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split('/')
        stack = []
        
        for char in words:
            if char == "" or char =='.':
                continue
            
            if char == "..":
                if stack:
                    stack.pop()
                continue
            
            stack.append(char)
        
        result = "/" + "/".join(stack)
        return result
            