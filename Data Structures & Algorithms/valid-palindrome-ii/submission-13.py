class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return ( self.isValid(left + 1, right, s) or self.isValid(left, right - 1, s))
            left += 1
            right -=1
        return True

    def isValid(self, left, right, s):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True

        