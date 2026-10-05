class Solution:
    def jump(self, nums: List[int]) -> int:
        jump, farthest, end = 0, 0 ,0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                end = farthest
                jump +=1
        
        return jump