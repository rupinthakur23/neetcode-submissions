class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for elem in operations:
            if elem not in ['+', 'C', 'D']:
                stack.append(elem)
                result += int(elem)
            elif elem =='+':
                top = stack[-1]
                second = stack[-2]
                output = int(top) + int(second)
                stack.append(output)
                result += output
            elif elem == 'D':
                top = stack[-1]
                output = 2 * int(top)
                stack.append(output)
                result += output
            elif elem == 'C':
                top = stack[-1]
                stack.pop()
                result -= int(top)
        return result



