class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        result = 0

        while left < right:
            if height[left] < height[right]:
                result += min(maxLeft, maxRight) - height[left]
                left +=1
                maxLeft = max(height[left], maxLeft)
            else:
                result += min(maxLeft, maxRight) - height[right]
                right -=1
                maxRight = max(height[right], maxRight)
        
        return result
