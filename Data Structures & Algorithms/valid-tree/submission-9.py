class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjaencyList = defaultdict(list)

        for u, v in edges:
            adjaencyList[u].append(v)
            adjaencyList[v].append(u)
        
        visited = set()
        q = deque([(0, 0)])
     
        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()

                visited.add(node)

                for nei in adjaencyList[node]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return False
                
                    q.append([nei, node])

        
        return True if len(visited) ==n  else False
        