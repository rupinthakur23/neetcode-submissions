class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        L = 0
        result = 0

        for R in range(len(s)):

            while(s[R] in store and store.get(s[R]) > 0):
                store[s[L]] -= 1
                L +=1   

            store[s[R]] = 1 + store.get(s[R], 0)
            result = max(result, R - L +1)
        
        return result
        