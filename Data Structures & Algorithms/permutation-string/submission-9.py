class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map, s2Map = [0] * 26, [0] * 26

        for char in s1:
            s1Map[ord(char) - ord('a')] += 1
        
        l = 0


        for r in range(len(s2)):
            s2Map[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) > len(s1):
                s2Map[ord(s2[l]) - ord('a')] -= 1
                l +=1

            if s1Map == s2Map:
                return True

        return False
