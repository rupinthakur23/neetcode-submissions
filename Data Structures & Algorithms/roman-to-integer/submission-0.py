class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        mapSet = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        for index in range(len(s)):
            if (index + 1) < len(s) and mapSet[s[index]] < mapSet[s[index + 1]]:
                result -= mapSet[s[index]]
            else:
                result += mapSet[s[index]]
        
        return result


        