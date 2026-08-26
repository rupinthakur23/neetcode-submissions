class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjanceyList = defaultdict(list)

        for uv, uw in edges:
            adjanceyList[uv].append(uw)
            adjanceyList[uw].append(uv)
        
        visited = set()
        result = 0

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            
            for nextNode in adjanceyList[node]:
                if nextNode in visited:
                    continue
                dfs(nextNode)
        
            return True

        for index in range(n):
            if dfs(index):
                result +=1
        
        return result