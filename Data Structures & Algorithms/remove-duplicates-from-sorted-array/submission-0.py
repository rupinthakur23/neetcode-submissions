class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        num = [nums[0]]
        for i in range(len(nums) - 1):
            if(nums[i]!= nums[i + 1]):
                count += 1
                num.append(nums[i + 1])
        for i in range(len(num)):
            nums[i] = num[i]
        
        return count
        