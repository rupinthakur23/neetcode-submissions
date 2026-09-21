class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            nums.append(i)
        
        result = 0
        
        for i in range(len(nums)):
            result = result  ^ nums[i]
        
        return result