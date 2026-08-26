class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while(left < right):
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return (self.isPalindrome( left + 1, right, s) or
                self.isPalindrome( left, right - 1, s))
        
        return True

    def isPalindrome(self, left, right, s):
        while(left < right):
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        return True
               