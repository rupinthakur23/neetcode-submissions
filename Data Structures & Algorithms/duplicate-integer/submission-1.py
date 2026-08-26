class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for num in nums:
            if num not in myMap:
                myMap[num] = 1
            else:
                return True
        return False