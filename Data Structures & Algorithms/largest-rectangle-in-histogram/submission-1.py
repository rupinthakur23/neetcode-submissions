class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxValue = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                popIndex, popHeight = stack.pop()
                maxValue = max(maxValue, (index - popIndex) * popHeight)
                start = popIndex

            stack.append([start, height])
        
        
        for index, height in stack: 
  
            maxValue = max(maxValue, (len(heights) - index) * height)
        

        return maxValue

