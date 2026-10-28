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

        def backtracking(i, word):
            if i == len(digits):
                result.append(word)
                return

            for char in digitsMap[digits[i]]:
                newWord = word + char
                backtracking(i + 1, newWord)


        if digits:
            backtracking(0, '')
        return result
        