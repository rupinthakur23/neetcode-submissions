class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        resultMap = {}

        for index in range(0, len(nums)):
            if nums[index] in resultMap:
                j = resultMap[nums[index]]
                if(abs(index - j) <=k):
                    return True
                resultMap[nums[index]] = index
            else:
               resultMap[nums[index]] = index
        return False