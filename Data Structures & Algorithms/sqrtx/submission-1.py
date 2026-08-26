class Solution:
    def mySqrt(self, x: int) -> int:
        ans = x
        left, right = 1, x

        while left <= right:
            mid = left + ((right - left)//2)

            if mid * mid <= x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
            
        
        return ans