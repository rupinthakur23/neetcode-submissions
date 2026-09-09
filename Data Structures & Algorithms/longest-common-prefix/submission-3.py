class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(strs)):
            for j in range(len(prefix)):
                while j < min(len(prefix), len(strs[i])):
                    if prefix[j] != strs[i][j]:
                        break
                    j +=1
                prefix = prefix[:j]
                if not prefix:
                    return ""
        
        return prefix