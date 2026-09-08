class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for index, value in enumerate(nums):
            if value in difference:
                ind = difference[value]
                return [ind, index]
            diff = target - value
            if diff not in difference:
                difference[diff] = index
            

