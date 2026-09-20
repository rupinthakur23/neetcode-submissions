class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            remainder = n % 2
            if remainder:
                result *= x
            
            x *= x
            n = n // 2
        
        return result