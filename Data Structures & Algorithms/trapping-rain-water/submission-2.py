class Solution:
    def trap(self, height: List[int]) -> int:
       left, right = 0, len(height) - 1
       maxLeft, maxRight = height[left], height[right]
       result = 0

       while left < right:
        if maxRight >= maxLeft:
            result += (min(maxRight, maxLeft) - height[left])
            left +=1
            maxLeft = max(maxLeft, height[left])
        else:
            result += (min(maxRight, maxLeft) - height[right])
            right -=1
            maxRight = max(maxRight, height[right])
  
       return result
