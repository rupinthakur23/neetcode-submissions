class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for value in paths:
            if value == '..':
                if stack:
                    stack.pop()
                continue
            
            if value != '.' and value != '':
                stack.append(value)
        return '/' + '/'.join(stack)