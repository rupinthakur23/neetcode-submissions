class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashMap = {}
        size = 0
        storeArray = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashMap[num] = hashMap.get(num, 0)  + 1
        
        for key, value in hashMap.items():
            storeArray[value].append(key)
        
        
        for num in storeArray[::-1]:
            if num:
                for item in num:
                    if size < k:
                        result.append(item)
                        size +=1
        
        return result

            