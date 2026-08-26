class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        for i in range(1, len(edges) + 1):
            parent[i] = i
            rank[i] = 0

        def find(n):
            par = parent[n]
            while par != parent[par]:
                par = parent[parent[par]]
            return par

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)


            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] +=1
            
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
            
