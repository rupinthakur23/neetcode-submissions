class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjaencyList = defaultdict(list)
        for i, q in enumerate(equations):
            adjaencyList[q[0]].append((q[1], values[i]))
            adjaencyList[q[1]].append((q[0], 1/values[i]))
        

        def bfs(src, tar):
            if src not in adjaencyList or tar not in adjaencyList:
                return - 1
            
            q = deque([(src, 1)])
            visited = set()

            while q:
                node, weight = q.popleft()
                if node == tar:
                    return weight
                
                visited.add(node)
                
                for nei, w in adjaencyList[node]:
                    if nei not in visited:
                        q.append((nei, weight * w))
                        visited.add(nei)
            return -1


        res = [bfs(src, tar) for src, tar in queries]
        return res
