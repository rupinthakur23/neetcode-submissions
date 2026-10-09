class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for index, char in enumerate(s):
            lastIndex[char] = index
        
        start, end = 0, 0
        result = []

        for index, char in enumerate(s):
            end = max(end,lastIndex[char])

            if index == end:
                result.append(end-start + 1)
                start = index + 1
        
        return result


