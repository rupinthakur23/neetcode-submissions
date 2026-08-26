class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, k, size = 0,1,0, len(nums) - 1

        while(right <= size):
            if(nums[left] != nums[right]):
                nums[k] = nums[left]
                k += 1
            left += 1
            right += 1
        nums[k] = nums[left]
        k += 1
        
        return k
