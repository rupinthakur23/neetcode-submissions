class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, char in enumerate(s):
            lastIndex[char] = i
        
        start, end = 0, 0
        result = []

        for i, char in enumerate(s):
            end = max(end, lastIndex[char])

            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
