class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, result = 0, len(heights) - 1, 0

        while left <= right:
            if heights[right] > heights[left]:
                result = max(result, min(heights[left], heights[right]) * (right - left))
                left +=1
            else:
                result = max(result, min(heights[left], heights[right]) * (right - left))
                right -=1
        
        return result