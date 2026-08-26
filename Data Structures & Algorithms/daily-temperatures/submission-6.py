class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temperature = stack.pop()
                result[index] = i - index
                
            stack.append([i, temperatures[i]])
        return result