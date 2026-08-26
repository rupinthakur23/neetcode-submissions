class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storerMap = {}

        for num in nums:
            if num in storerMap:
                return True
            else:
                storerMap[num] = 1
        return False