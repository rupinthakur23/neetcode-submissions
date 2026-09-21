class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber = columnNumber - 1

            offset = columnNumber % 26

            digit = result.append(chr(offset + ord('A')))

            columnNumber = columnNumber // 26
        
        return ''.join(reversed(result))