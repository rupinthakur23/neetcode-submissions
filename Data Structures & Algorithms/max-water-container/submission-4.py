class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result, left, right = 0, 0, len(heights) - 1

        while left < right:
            result = max( (min(heights[left], heights[right]) * (right - left)), result)

            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
        
        return result