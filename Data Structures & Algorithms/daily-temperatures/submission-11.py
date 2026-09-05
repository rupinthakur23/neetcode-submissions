class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                ind, temp = stack.pop()
                result[ind] = index - ind

            stack.append([index, temperature])
        
        return result

