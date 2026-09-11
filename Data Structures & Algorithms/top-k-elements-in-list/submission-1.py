class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        freqMap = defaultdict(list)
        result = []

        for num in nums:
            countMap[num] +=1
        
        for key, value in countMap.items():
            freqMap[value].append(key)

        for key in sorted(freqMap.keys(), reverse=True):
            if key:
                for val in freqMap[key]:
                    if len(result) < k:
                        result.append(val)
        
        return result
        
        
        


        
