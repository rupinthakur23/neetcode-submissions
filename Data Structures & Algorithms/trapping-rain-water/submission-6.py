class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, result = 0, len(height) - 1, 0
        maxLeft, maxRight = height[left], height[right]

        while left <= right:
            if maxLeft < maxRight:
                result +=  min(maxLeft, maxRight) - height[left] 
                left +=1
                maxLeft = max(maxLeft, height[left])
            else:
                result +=  min(maxLeft, maxRight) - height[right] 
                right -=1
                maxRight = max(maxRight, height[right])
        
        return result

        