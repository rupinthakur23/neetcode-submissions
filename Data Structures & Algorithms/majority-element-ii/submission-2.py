class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

            if len(countMap) > 2:
                newMap = {}
                for key, value in countMap.items():
                    if value > 1:
                        newMap[key] = value -1
                countMap = newMap
        
        result = []

        for key in countMap.keys():
            if nums.count(key) > len(nums) //3:
                result.append(key)
        
        return result