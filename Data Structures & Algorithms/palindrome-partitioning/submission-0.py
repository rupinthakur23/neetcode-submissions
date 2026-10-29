class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, curList = [], []

        def backtracking(i):
            if i >= len(s):
               result.append(curList.copy())
               return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curList.append(s[i:j + 1])
                    backtracking(j + 1)
                    curList.pop()


        backtracking(0)
        return result

    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i +=1
            j-=1
        return True
