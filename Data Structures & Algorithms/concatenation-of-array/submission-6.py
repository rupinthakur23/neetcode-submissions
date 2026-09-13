class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * (2 * length)

        for index, value in enumerate(nums):
            result[index] = value
            result[index + length] = value
        return result