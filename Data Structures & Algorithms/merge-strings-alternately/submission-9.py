class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        left, right = 0, 0

        while len(word1) > left or len(word2) > right:
            if len(word1) > left:
                result.append(word1[left])
                left +=1

            if len(word2) > right:
                result.append(word2[right])
                right +=1
        
        return "".join(result)
            
