class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currSet, resultSet = [], []


        def dfs(index, currSet, resultSet):
            if len(currSet) == k:
                resultSet.append(currSet.copy())
                return
            if index > n:
                return
            
            for i in range(index, n + 1):
                currSet.append(i)
                dfs(i + 1, currSet, resultSet)
                currSet.pop()

        dfs(1,currSet, resultSet)
        return resultSet