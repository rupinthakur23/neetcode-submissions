class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float('inf')
        output = 0

        for R in range (len(nums)):
            output += nums[R]

            while(output >= target):
                length = min(length, R - L + 1)
                output -= nums[L]
                L += 1

        return 0 if length == float('inf') else length