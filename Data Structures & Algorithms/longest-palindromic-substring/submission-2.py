class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        resultWindow = []
        def findPalindrome( l, r):
            nonlocal result, resultWindow
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result:
                    result = r - l + 1
                    resultWindow = [l, r]
                l -= 1
                r +=1

        for i in range(len(s)):
            findPalindrome(i, i)
            findPalindrome(i, i + 1)
        l, r = resultWindow
        return s[l : r + 1]

            
