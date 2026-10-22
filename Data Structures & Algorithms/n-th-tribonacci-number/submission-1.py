class Solution:
    def tribonacci(self, n: int) -> int:
        if n <=2:
            if n == 0:
                return 0
            else:
                return 1
        
        dp = [0,1,1]

        for _ in range(3, n + 1):
            temp1, temp2 = dp[1], dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0], dp[1] = temp1, temp2 
        
        return dp[2]