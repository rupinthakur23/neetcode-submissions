class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right, count = 0, len(nums) - 1 , 0

        while(left <= right):
            if(nums[left] == val and nums[left] == nums[right]):
                right -= 1
            elif(nums[left] == val):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                count += 1
            else:
                left += 1
                count += 1
        return count