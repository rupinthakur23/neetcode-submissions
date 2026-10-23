class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitsMap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtracking(index, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            print(index)
            for c in digitsMap[digits[index]]:
                backtracking(index + 1, curStr + c)

        if digits:
            backtracking(0, '')
        return result
        