class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            n = len(nums)
        
            dp = [0] * (n + 2)
            
            for i in range(n - 1, -1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            
            return dp[0]
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

