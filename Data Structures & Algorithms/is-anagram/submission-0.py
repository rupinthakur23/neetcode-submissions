
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False;
        countsS, countsT = {}, {}
        
        for char in range(len(s)):
            countsS[s[char]] = 1 +  countsS.get(s[char], 0)
            countsT[t[char]] = 1 +  countsT.get(t[char], 0)
        
        return countsS == countsT

        