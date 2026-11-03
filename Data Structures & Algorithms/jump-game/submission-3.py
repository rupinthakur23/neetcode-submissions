class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= steps:
                steps = i
        
        return steps == 0