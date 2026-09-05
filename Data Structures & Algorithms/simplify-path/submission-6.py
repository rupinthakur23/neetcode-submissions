class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for path in paths:
            if path == '..':
                if stack:
                    stack.pop()
            else:
                if path != '' and path != '.':
                    stack.append(path)
        
        return '/' + '/'.join(stack)
