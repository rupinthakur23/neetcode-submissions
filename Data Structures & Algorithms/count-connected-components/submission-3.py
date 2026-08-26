class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ajaencyList = defaultdict(list)

        for uv, uw in edges:
            ajaencyList[uv].append(uw)
            ajaencyList[uw].append(uv)
        
        courseMap = [False] * n

        result = 0

        def dfs(node):

            if courseMap[node]:
                return
        
            courseMap[node] = True
            for nei in ajaencyList[node]:
                if not courseMap[nei]:
                    dfs(nei)
            
            return
        

        for i in range(n):
            if not courseMap[i]:
                courseMap[i] = True
                for nei in ajaencyList[i]:
                    dfs(nei)
                result +=1
        return result