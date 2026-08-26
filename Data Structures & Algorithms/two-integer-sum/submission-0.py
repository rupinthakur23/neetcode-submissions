class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        result = [0] * 2

        for index, value in enumerate(nums):
            if value in differences:
                result = [differences[value], index]
            else:
                differences[target - value] = index
        return result
        