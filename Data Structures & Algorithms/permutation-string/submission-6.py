class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        sCount1, sCount2 = [0] * 26, [0] * 26

        for l in range(len(s1)):
            sCount1[ord(s1[l]) - ord('a')] += 1
            sCount2[ord(s2[l]) - ord('a')] += 1
        
        matches = 0
        
        for i in range(26):
            matches += (1 if sCount1[i] == sCount2[i] else 0)
        
        l = 0

        for r in range(len(s1), len(s2)):
            if (matches == 26): return True

            index = ord(s2[r]) - ord('a')
            sCount2[index] += 1

            if(sCount2[index] == sCount1[index]):
                matches+=1
            elif sCount1[index] + 1 == sCount2[index]:
                matches-=1

            index = ord(s2[l]) - ord('a')
            sCount2[index] -= 1

            if(sCount2[index] == sCount1[index]):
                matches+=1
            elif sCount1[index] - 1 == sCount2[index]:
                matches-=1
            l +=1
        
        return matches == 26
            

