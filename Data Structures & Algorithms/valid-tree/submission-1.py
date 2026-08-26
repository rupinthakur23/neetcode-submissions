class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ajacencyList = {i:[] for i in range(n)}

        for uv, uw in edges:
            ajacencyList[uv].append(uw)
            ajacencyList[uw].append(uv)
        
        q = deque([(0, 0)])
        visited = set()        
        
        while q:
            node, parentNode = q.popleft()
            if node in visited:
                return False
            
            visited.add(node)

            for nextNode in ajacencyList[node]:
                if nextNode != parentNode:
                    q.append((nextNode, node))
    
        return True if len(visited) == n else False

