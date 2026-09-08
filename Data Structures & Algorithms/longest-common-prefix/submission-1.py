class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while(j < min(len(result), len(strs[i]))):
                if result[j] != strs[i][j]:
                    break
                j += 1
            result = result[:j]
            
            if not result:
                return ""
        return result
