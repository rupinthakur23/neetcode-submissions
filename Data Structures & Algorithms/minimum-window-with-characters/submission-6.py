class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap, tMap = defaultdict(int), defaultdict(int)

        for char in t:
            tMap[char] += 1
        
        keen, have = len(tMap), 0
        l, result, boundary = 0,float('inf'), [-1, -1]

        for r in range(len(s)):
            sMap[s[r]] += 1

            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have +=1
            
            while have == keen:
                length = r - l + 1
                if length < result:
                    result = length
                    boundary = [l, r]
   
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -=1
                l+=1
        
        start, end = boundary

        return '' if result == float('-inf') else s[start:end + 1]
                
