class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        groupMap = defaultdict(list)
        result = []

        for num in nums:
            countMap[num] +=1
        
        for key, value in countMap.items():
            groupMap[value].append(key)
        
        for key in sorted(groupMap.keys(), reverse=True):
            for item in groupMap[key]:
                if len(result) < k:
                    result.append(item)
        
        return result
        