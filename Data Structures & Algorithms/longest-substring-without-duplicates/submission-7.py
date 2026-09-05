class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        result, l = 0, 0

        for r in range(len(s)):

            while s[r] in visited:
                visited.remove(s[l])
                l +=1 

            result = max(result, r - l + 1)
            visited.add(s[r])
        
        return result