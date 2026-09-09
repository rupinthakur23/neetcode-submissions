class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap, left, right = 0, 0, len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                nums[swap], nums[left] = nums[left], nums[swap]
                swap +=1
                left +=1
            elif nums[left] == 2:
                nums[right], nums[left] = nums[left], nums[right]
                right -=1
            else:
                left +=1
        
        return nums
        