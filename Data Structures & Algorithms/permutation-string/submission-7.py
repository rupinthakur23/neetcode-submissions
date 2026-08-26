class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        resultMap1= {}
        resultMap2= {}


        for char in s1:
            resultMap1[char] =  resultMap1.get(char, 0) + 1
        
        left = 0

        for right in range(len(s2)):
            resultMap2[s2[right]] =  resultMap2.get(s2[right], 0) + 1

            if(right - left + 1 == len(s1)):
                counter = 0
                if resultMap1 == resultMap2:
                    return True
                    
                resultMap2[s2[left]] -=1
                if resultMap2[s2[left]] == 0:
                    del resultMap2[s2[left]]
                left +=1
                

        return False
