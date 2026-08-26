class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}

        for c in range(len(t)):
            countT[t[c]] = 1 + countT.get(t[c], 0)
        have, keen = len(countT), 0
        l = 0
        result, resultLen = [-1,-1], float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                keen+=1
            
            while( keen == have):
                if(r - l + 1 < resultLen):
                    result = [l,r]
                    resultLen = r - l + 1
                m = s[l]
                window[s[l]] -= 1
                if m in countT and window[m] < countT[m]:
                    keen-=1
                l+=1
        
        l, r = result
        return s[l:r+1] if resultLen != float('inf') else ""

