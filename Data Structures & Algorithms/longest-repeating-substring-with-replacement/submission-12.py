class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       countMap = {}
       left, maxCount, result = 0,0,0

       for right in range(len(s)):
        countMap[s[right]] = countMap.get(s[right], 0) + 1
        maxCount = max(countMap.values())

        while (right - left + 1) - maxCount > k:
           countMap[s[left]] -=1
           left +=1
        
        result = max(result, right - left + 1)

       return result
