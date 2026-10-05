class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, globalMax, maxSum, minSum, globalMin = nums[0], nums[0], nums[0],nums[0], nums[0]

        for i in range(1,len(nums)):
            total += nums[i]

            maxSum = max(maxSum, 0)
            maxSum += nums[i]
            globalMax = max(maxSum, globalMax)

            minSum = min(minSum, 0)
            minSum += nums[i]
            globalMin = min(minSum, globalMin)
        
        if globalMax < 0:
            return globalMax
        
        return max(globalMax, total - globalMin)