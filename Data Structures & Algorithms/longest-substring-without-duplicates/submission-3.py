class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        store = set()

        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left+=1
            
            store.add(s[right])
            result = max(result, right - left + 1)
        
        return result
