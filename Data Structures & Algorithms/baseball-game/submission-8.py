class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for operation in operations:
            if operation == '+':
                result.append(result[-1] + result[-2])
            elif operation == 'D':
                result.append(result[-1] * 2)
            elif operation == 'C':
                result.pop()
            else:
                result.append(int(operation))
        
        return sum(result)
            