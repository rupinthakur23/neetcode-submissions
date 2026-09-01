class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap, TMap= {}, {}
        minWindow, minimum = [-1, -1], float("inf")

        for char in t:
            TMap[char] = TMap.get(char, 0) + 1
        
        keen = len(TMap)
        have = 0

        l = 0

        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1

            if s[r] in TMap and sMap[s[r]] == TMap[s[r]]:
                have +=1
            
            while have == keen:
                if ( r - l + 1) < minimum:
                    minWindow = [r, l]
                    minimum = r - l + 1

                sMap[s[l]] -=1

                if s[l] in TMap and sMap[s[l]] < TMap[s[l]]:
                    have -=1
                l +=1

        return s[minWindow[1]: minWindow[0] + 1] if minimum != float("inf") else ""
            


