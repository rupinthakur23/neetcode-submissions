class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for elem in tokens:
            if elem == '+':
                stack.append(stack.pop() + stack.pop())
            elif elem == '-':
                a, b = stack.pop(), stack.pop()
                stack.append( b - a)
            elif elem == '*':
                stack.append(stack.pop() * stack.pop())
            elif elem == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(elem))
        return stack[0]