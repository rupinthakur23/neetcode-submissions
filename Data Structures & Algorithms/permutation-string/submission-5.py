class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count  = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 +  s1Count.get(s1[i], 0)   
        need = len(s1Count)
        for i in range(len(s2)):
            s2Count = {}
            count = 0
            for j in range(i,len(s2)):
                s2Count[s2[j]] = 1 +  s2Count.get(s2[j], 0) 
                if(s1Count.get(s2[j], 0) < s2Count.get(s2[j])):
                    break;
                elif ( s1Count.get(s2[j], 0) == s2Count.get(s2[j])):
                    count +=1
                if need == count:
                    return True
        
        return False

