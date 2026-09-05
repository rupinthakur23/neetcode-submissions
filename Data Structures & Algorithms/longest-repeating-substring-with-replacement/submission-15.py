class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq = 0
        result, l = 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            if (r - l + 1) - maxFreq > k:
                freq[s[l]] -=1
                l +=1

            result = max( result, r - l + 1)
        
        return result