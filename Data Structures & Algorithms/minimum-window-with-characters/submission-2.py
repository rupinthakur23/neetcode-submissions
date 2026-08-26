class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount, tCount = {}, {}
        for char in t:
            tCount[char] = 1 + tCount.get(char,0)
        keen, have = 0, len(tCount)
        minWindow, minLength = [-1,-1], float('inf')

        left = 0

        for right in range(len(s)):
            char = s[right]
            sCount[char] = 1 + sCount.get(char,0)
            
            if char in tCount and sCount[char] == tCount[char]:
                keen+=1
            
            while( have == keen):
                if(right - left +1 < minLength):
                    minWindow = [left, right]
                    minLength = right - left +1

                remChar = s[left]
                sCount[remChar] -= 1

                if remChar in tCount and sCount[remChar] < tCount[remChar]:
                    keen -=1
                
                left+=1
        
        left, right = minWindow
        return s[left:right + 1] if minLength!= float('inf') else ""

            
