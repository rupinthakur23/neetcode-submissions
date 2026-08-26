class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while(left < right):
            if s[left] != s[right]:
                return (self.checkPalindrome(s, left + 1, right) or
                    self.checkPalindrome(s, left, right - 1))
            else:
                left +=1
                right -=1
        return True


    def checkPalindrome(self, s, left, right):
        while(left < right):
            if s[left] != s[right]:
                return False
            else:
                left +=1
                right -=1
        return True