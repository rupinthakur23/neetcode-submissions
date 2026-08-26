class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result, stack = 0, []
        activeOperations = ["+", "C", "D"]

        for val in operations:
            if val not in activeOperations:
                stack.append(int(val))
                result += int(val)
            else:
                if val == '+':
                    first, second = stack[-1], stack[-2]
                    newElement = first + second
                    stack.append(newElement)
                    result += newElement
                elif val == 'C':
                    result -= stack[-1]
                    stack.pop()
                else:
                    newElement = stack[-1] * 2
                    stack.append(newElement)
                    result += newElement
        
        return result
                    
