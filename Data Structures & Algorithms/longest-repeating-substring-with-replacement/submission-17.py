class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = defaultdict(int)
        l, result, maxCount = 0, 0, 0

        for r in range(len(s)):
            countMap[ord(s[r]) - ord('A')] +=1
            maxCount = max(maxCount, countMap[ord(s[r]) - ord('A')])

            while ((r - l + 1) - maxCount) > k:
                countMap[ord(s[l]) - ord('A')] -=1
                l +=1
            
            result = max(result, r - l + 1)
        return result
