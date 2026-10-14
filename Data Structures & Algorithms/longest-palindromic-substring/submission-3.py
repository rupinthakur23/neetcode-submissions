class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        window = [-1, -1]

        for i in range(len(s)):
            l = r = i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result:
                    result = r - l + 1
                    window = [l, r]
                l -=1
                r +=1
    
            l, r =i,  i + 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result:
                    result = r - l + 1
                    window = [l, r]
                l -=1
                r +=1
        return s[window[0]:window[1] + 1 ]