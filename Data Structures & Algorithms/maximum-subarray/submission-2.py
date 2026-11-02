class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, float('-inf')

        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        
        return maxSum
        