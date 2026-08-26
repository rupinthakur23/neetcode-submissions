class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, result = 0, len(heights) - 1, 0

        while left < right:

            result = max(min(heights[left], heights[right]) * (right - left), result)
            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
        
        return result