class Solution:
    def partition(self, s: str) -> List[List[str]]:
        resultList, currList = [], []

        def backtracking(i):
            if i == len(s):
                resultList.append(currList.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    currList.append(s[i:j +1])
                    backtracking(j + 1)
                    currList.pop()

        backtracking(0)
        return resultList
    

    def isPalindrome(self, l, r, s):
        while l <= r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True
