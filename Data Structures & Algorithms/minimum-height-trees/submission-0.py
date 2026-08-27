class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adjaencyList = defaultdict(list)

        for uv, uw in edges:
            adjaencyList[uv].append(uw)
            adjaencyList[uw].append(uv)
        
        leaves = deque()

        nodeCount = {}

        for src, nei in adjaencyList.items():
            if len(nei) == 1:
                leaves.append(src)
            nodeCount[src] = len(nei)
        
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1

                for nei in adjaencyList[node]:
                    nodeCount[nei] -=1
                    if nodeCount[nei] ==1 :
                        leaves.append(nei)

