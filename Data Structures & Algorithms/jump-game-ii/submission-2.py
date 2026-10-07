class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, endPoint, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == endPoint:
                jumps+=1
                endPoint = farthest
        
        return jumps