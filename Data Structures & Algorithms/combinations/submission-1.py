class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, currSet = [], []

        def dfs(index):
            if len(currSet) == k:
                result.append(currSet.copy())
                return
            
            if index > n:
                return
        
            
            for i in range(index, n + 1):
                currSet.append(i)
                dfs(i + 1)
                currSet.pop()

        dfs(1)
        return result
        