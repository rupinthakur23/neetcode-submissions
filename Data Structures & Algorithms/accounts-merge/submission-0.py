class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]    
        return node

    def union(self,node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return False
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.parent[par1] = par2
            self.rank[par2] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailMap = {}
        for i, a in enumerate(accounts):
            for e in accounts[i][1:]:
                if not e in emailMap:
                    emailMap[e] = i
                else:
                    uf.union(i, emailMap[e])
        emailGroup = defaultdict(list)
        for e, i in emailMap.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []

        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res

        

