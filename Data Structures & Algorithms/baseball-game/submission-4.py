class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for elem in operations:
            if elem == '+':
                stack.append(stack[-1] + stack[-2])
            elif elem == 'C':
                stack.pop()
            elif elem == 'D': 
                stack.append(2 * stack[-1])
            else:
                stack.append(int(elem))
        
        return sum(stack)

        