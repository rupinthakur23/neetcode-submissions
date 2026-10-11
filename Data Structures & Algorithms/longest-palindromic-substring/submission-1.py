class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        resultWindow = []

        for i in range(len(s)):
            l = r = i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result:
                    result = r - l + 1
                    resultWindow = [l, r]
                l -= 1
                r +=1

            l, r = i, i + 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result:
                    result = r - l + 1
                    resultWindow = [l, r]
                l -= 1
                r +=1
        l, r = resultWindow
        return s[l : r + 1]
            
