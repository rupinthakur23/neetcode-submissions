class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap = 0
        for num in nums:
            if num!= val:
                nums[swap] = num
                swap +=1
        return swap