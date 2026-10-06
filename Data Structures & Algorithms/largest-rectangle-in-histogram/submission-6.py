class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, result = [], 0

        for index, height in enumerate(heights):
            newIndex = index
            while stack and stack[-1][1] > height:
                oldIndex, oldHeight = stack.pop()
                result = max((index - oldIndex) * oldHeight, result)
                newIndex = oldIndex
        
            stack.append([newIndex, height])
        

        for index, height in stack:
            result = max((len(heights) - index) * height, result)
        
        return result