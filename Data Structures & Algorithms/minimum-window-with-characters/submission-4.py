class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap, tMap = {}, {}
        l = 0
        window, minimum = [-1,-1], float("inf")

        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        
        have, keen = len(tMap), 0

        for r in range(len(s)):
            char = s[r]
            sMap[char] = sMap.get(char, 0) + 1

            if char in tMap and sMap[char] == tMap[char]:
                keen +=1
            
            while have == keen:
                if (r - l + 1) < minimum:
                    window = [r,l]
                    minimum = r - l + 1
                
                popChar = s[l]
                sMap[popChar] -=1
                if popChar in tMap and sMap[popChar] < tMap[popChar]:
                    keen -=1
                l +=1
        print(window)
        
        end, start = window
        return "" if minimum == float("inf") else s[start: end + 1]
            
            


            
