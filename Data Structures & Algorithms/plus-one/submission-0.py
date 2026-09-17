class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry

            digit = total % 10
            carry = total // 10
            result.append(digit)
        
        if carry:
            result.append(carry)
        
        return list(reversed(result))


