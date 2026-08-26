class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        left, right = 0, 0
        result = []

        while left < n1 or right < n2:
            if left < n1:
                result.append(word1[left])
                left +=1
            
            if right < n2:
                result.append(word2[right])
                right +=1
        
        return ''.join(result)

