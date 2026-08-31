class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result, l, maxFreq = float("-inf"), 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(count[s[r]], maxFreq)

            if (r -l + 1) - maxFreq >k:
                count[s[l]] -=1
                l +=1

            result = max(result, r - l + 1)
        
        return 0 if result == float("-inf") else result
            
