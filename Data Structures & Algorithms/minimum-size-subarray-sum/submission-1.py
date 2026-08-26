class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        L, output = 0, 0

        for R in range(len(nums)):
            output += nums[R]

            while(output >= target):
                result = min(R- L + 1, result)
                output -= nums[L]
                L+= 1
        
        return result if result!= float('inf') else 0

        