class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjaencyList = defaultdict(list)
        count = 0
        for u, v in edges:
            adjaencyList[u].append(v)
            adjaencyList[v].append(u)
        
        edgeFlag = [True] * n
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            edgeFlag[node] = False

            for nei in adjaencyList[node]:
                dfs(nei)


        for i in range(n):
            if edgeFlag[i]:
                dfs(i)
                count +=1
        
        return count