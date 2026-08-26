class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultStack = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                print(value)
                print(stack[-1][1])
                index, val = stack.pop()
                resultStack[index] = i - index
            stack.append((i, value))
            print(stack)
        
        return resultStack