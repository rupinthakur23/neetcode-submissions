class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,m,n = 0,0,len(word1), len(word2)
        result = []

        for i in range(max(m,n)):
            if i < m:
                result.append(word1[i])
            if i <n:
                result.append(word2[i])   

        return "".join(result)      