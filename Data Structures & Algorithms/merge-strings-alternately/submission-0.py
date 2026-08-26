class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left,right,m,n = 0,0,len(word1), len(word2)
        result = []

        while(left<m or right <n):
            if(left < m):
                result.append(word1[left])
                left += 1
            if(right <n):
                result.append(word2[right])
                right += 1
        return "".join(result)
            

