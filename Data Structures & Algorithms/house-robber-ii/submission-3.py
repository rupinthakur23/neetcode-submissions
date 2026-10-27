class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def partRob(num):
            dp = [0] * (len(num) + 2)
            print(dp)

            for i in range(len(dp) - 3, -1, -1):
                dp[i] = max(dp[i + 1], num[i] + dp[i + 2])
            return max(dp[0], dp[1])
        

        return max(partRob(nums[:-1]), partRob(nums[1:]))

