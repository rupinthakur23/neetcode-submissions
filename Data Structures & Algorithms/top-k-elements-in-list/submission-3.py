class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        result = []
        countMap = defaultdict(list)

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for key, value in freqMap.items():
            countMap[value].append(key)
        
        for key in sorted(countMap.keys(), reverse=True):
            for val in countMap[key]:
                if len(result) < k:
                    result.append(val)
        
        return result
