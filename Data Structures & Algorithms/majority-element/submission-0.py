class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

            if countMap[num] > len(nums)/2:
                return num