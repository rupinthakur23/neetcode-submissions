class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]

        for num in nums:
            temp = curMax * num
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, temp, curMin * num)
            res = max(res, curMax)
        
        return res