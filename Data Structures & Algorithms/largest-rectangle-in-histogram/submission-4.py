class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for index, height in enumerate(heights):
            i = index
            while stack and stack[-1][0] > height:
                newHeight, i = stack.pop()
                result = max(result, newHeight * ( index - i))
            index = i

            stack.append((height, index))
        
        for height, index in stack:
            result = max(result, height * (len(heights) - index))
        
        return result






