class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        result = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            if (R - L + 1) - max(count.values()) <=k:
                result = max(result, R - L + 1)
            else:
                count[s[L]] -= 1
                L += 1
            
        return result

