class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False;

        mapS , mapT = {}, {}

        for char in range(len(s)):
            mapS[s[char]] = 1 + mapS.get(s[char], 0)
            mapT[t[char]] = 1 + mapT.get(t[char], 0)
        
        return mapS == mapT


        