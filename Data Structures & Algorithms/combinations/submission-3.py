class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset, currset = [], []

        def backtracking(i):
            if len(currset) == k:
                subset.append(currset.copy())
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                currset.append(j)
                backtracking(j + 1)
                currset.pop()
        
        backtracking(1)
        return subset