class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        a, b = a[::-1], b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            aDigit = int(a[i]) if i < len(a) else 0 
            bDigit = int(b[i]) if i < len(b) else 0 

            total = aDigit + bDigit + carry
            char = str(total % 2)
            result = char + result
            carry = total //2
        
        if carry:
            return '1' + result
        
        return result
        