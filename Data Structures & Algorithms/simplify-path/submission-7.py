class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for path in paths:
            if path == '..':
                if stack:
                    stack.pop()
            else:
                if path == '' or path == '.':
                    continue
                else:
                    stack.append(path)
        
        return '/' + '/'.join(stack)
