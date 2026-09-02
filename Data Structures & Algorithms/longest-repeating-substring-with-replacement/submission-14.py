class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, result, sMap= 0, float("-inf"), {}
        maxFreq = 0

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1

            maxFreq = max(maxFreq, sMap[s[r]])

            while ((r - l + 1) - maxFreq) > k:
                sMap[s[l]] -=1
                l +=1
            
            result = max(result, r - l + 1)
        
        return 0 if result == float("-inf") else result

