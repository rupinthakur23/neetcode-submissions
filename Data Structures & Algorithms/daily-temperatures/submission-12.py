class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                oldIndex, oldTemp = stack.pop()
                result[oldIndex] = index - oldIndex

            stack.append([index, temp])
        return result