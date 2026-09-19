class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = nums[0], nums[0]

        for num in nums[1:]:
            curSum = max(curSum, 0)
            curSum += num
            maxSum = max(maxSum, curSum)
        
        return maxSum
                    