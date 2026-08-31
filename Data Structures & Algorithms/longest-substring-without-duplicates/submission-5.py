class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, result = 0, float("-inf")

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l +=1

            visited.add(s[r])
            result = max(result, (r - l) + 1)
        
        return 0 if result == float("-inf") else result