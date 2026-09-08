class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ajcaencyList = defaultdict(list)
        for uv, uw in edges:
            ajcaencyList[uv].append(uw)
            ajcaencyList[uw].append(uv)  

        nodesMap = [False] * n

        result = 0
        def dfs(node):

            nodesMap[node] = True
            
            for nei in ajcaencyList[node]:
                if nodesMap[nei]:
                    continue
                dfs(nei)
            return

        for i in range(n):
            if not nodesMap[i]:
                result +=1
                dfs(i)
        return result
