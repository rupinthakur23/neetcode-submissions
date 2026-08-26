class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,m,n = 0,0,len(word1), len(word2)
        result = []
        while(i < m or j <n):
            if(i < m):
                result.append(word1[i])

            if(j < n):
                result.append(word2[i])
            
            i +=1
            j +=1
        
        return "".join(result)