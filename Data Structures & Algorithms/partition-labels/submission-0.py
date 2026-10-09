class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapIndex = defaultdict(int)
        size, end = 0, 0
        result = []

        for i in range(len(s)):
            mapIndex[s[i]] = i
        
        for i in range(len(s)):
            end = max(end, mapIndex[s[i]])

            if i == end:
                result.append(size + 1)
                size = 0
            else:
                size +=1

        return result
