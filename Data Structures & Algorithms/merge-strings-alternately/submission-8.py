class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        m, n = 0, 0

        while m < len(word1) or n < len(word2):
            if m < len(word1):
                result.append(word1[m])
                m +=1

            if n < len(word2):
                result.append(word2[n])
                n +=1

        return "".join(result)            