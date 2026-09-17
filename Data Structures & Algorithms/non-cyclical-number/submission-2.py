class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 0:
            visited.add(n)
            if n ==1:
                return True
            n = self.sumOfSquares(n)
            if n in visited:
                return False
    

    def sumOfSquares(self, n):
        result = 0

        while n > 0:
            digit = n % 10
            result += digit ** 2
            n = n //10
        return result
    