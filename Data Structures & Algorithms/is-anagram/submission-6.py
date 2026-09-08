class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        sMap = [0] * 26
        tMap = [0] * 26

        for char in s:
            sMap[ord(char) - ord('a')] +=1

        for char in t:
            tMap[ord(char) - ord('a')] +=1
        
        return sMap == tMap
        

