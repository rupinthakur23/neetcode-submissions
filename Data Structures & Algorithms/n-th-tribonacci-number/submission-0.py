class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 2 or n ==1:
            return 1
        
        if n == 0:
            return 0
        
        dp = [0,1,1]

        i = 3

        while i <= n:
            tmp2, tmp3 =  dp[1], dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]

            dp[1] = tmp3
            dp[0] = tmp2
            i +=1
        
        return dp[2]

            