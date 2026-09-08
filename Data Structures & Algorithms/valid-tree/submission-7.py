class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ajcaencyList = defaultdict(list)
        for uv, uw in edges:
            ajcaencyList[uv].append(uw)
            ajcaencyList[uw].append(uv)
        
        q = deque([(0, 0)])
        visited = set()

        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()

                visited.add(node)
                
                for nei in ajcaencyList[node]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return False
                    
                    q.append([nei, node])
        return False if len(visited) != n else True
                    

                    

                