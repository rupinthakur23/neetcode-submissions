class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMax, curMin = 1,1

        for num in nums:
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            result = max(curMax, result)
        
        return result