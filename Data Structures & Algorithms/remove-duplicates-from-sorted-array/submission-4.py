class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, insert = 1, 1
        if ( len(nums) == 1):
            return 1

        while(left < len(nums)):
            if(nums[left] != nums[left -1]):
                nums[insert] = nums[left]
                insert += 1
            left +=1
        
        return insert
            