class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}  # count of chars in current window
        counter = 0      # max frequency of any char in window
        L = 0
        output = 0

        for R in range(len(s)):
            dictionary[s[R]] = 1 + dictionary.get(s[R], 0)
            counter = max(counter, dictionary[s[R]])

            if (R - L + 1) - counter > k:
                dictionary[s[L]] -= 1
                L += 1
            
            output = max(output, R - L + 1)
        
        return output
