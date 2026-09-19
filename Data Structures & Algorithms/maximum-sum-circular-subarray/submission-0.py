class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, curMax, curMin, globalMax, globalMin = nums[0], nums[0], nums[0], nums[0], nums[0]

        for num in nums[1:]:
            total += num

            curMax = max(curMax, 0)
            curMax += num
            globalMax = max(globalMax, curMax)

            curMin = min(curMin, 0)
            curMin += num
            globalMin = min(globalMin, curMin)
        
        if globalMax < 0:
            return globalMax
        
        return max(globalMax, total - globalMin )

