class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while(left < right):
            while(left<right and not self.alphanumeric(s[left])):
                left += 1

            while(right >left  and not self.alphanumeric(s[right])):
                right -= 1
            if(s[left].lower() == s[right].lower()):
                left +=1
                right -=1
            else:
                return False
        return True
        
    def alphanumeric(self, character):
        return (ord('A') <= ord(character) <= ord('Z') or
                ord('a') <= ord(character) <= ord('z') or
                ord('0') <= ord(character) <= ord('9'))