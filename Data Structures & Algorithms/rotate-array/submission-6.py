class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        k = k % len(nums)
        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left , right = 0, k -1
        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left, right = k, len(nums) - 1
        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        