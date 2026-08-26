class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, output = 0, 0
        minResult = float("inf")

        for right in range(len(nums)):
            output += nums[right]

            while(output >= target):
                minResult = min ( (right - left + 1), minResult)
                output -= nums[left]
                left+=1
        
        return 0 if minResult == float("inf") else minResult