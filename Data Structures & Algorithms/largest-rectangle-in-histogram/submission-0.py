class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxFrequency = [], 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, value = stack.pop()
                maxFrequency = max(maxFrequency, value * (i - index))
                start = index
            
            stack.append((start, h))

        
        for i, h in stack:
            maxFrequency = max(maxFrequency, h * (len(heights) - i))
        
        return maxFrequency