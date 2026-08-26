class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output, stack = [0] * len(temperatures), []

        for index, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                diff = index - stack[-1]
                output[stack[-1]] = diff
                stack.pop()
            stack.append(index)
        return output