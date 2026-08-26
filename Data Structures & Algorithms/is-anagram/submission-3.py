class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)): return False
        disctionaryS, disctionaryT = {}, {}

        for char in s:
            disctionaryS[char] = disctionaryS.get(char, 0) + 1

        for char in t:
            disctionaryT[char] = disctionaryT.get(char, 0) + 1

        for char in s:
            if(disctionaryS.get(char) != disctionaryT.get(char, 0)):
                return False
        
        return True
        