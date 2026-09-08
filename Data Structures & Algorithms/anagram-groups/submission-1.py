class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strsCounter = [[0] * 26 for i in strs]
        resultMap = {}
        result = []

        for i, string in enumerate(strs):
            for char in string:
                strsCounter[i][ord(char) - ord('a')] +=1
            
            key = tuple(strsCounter[i])
            
            if key not in resultMap:
                resultMap[key] = []
            resultMap[key].append(string)
        
        for value in resultMap.values():
            result.append(value)
        
        return result



