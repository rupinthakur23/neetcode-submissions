class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and stack [-1][0] < temperature:
                temp, index = stack.pop()
                result[index] = i -index

            stack.append((temperature, i))
        
        return result