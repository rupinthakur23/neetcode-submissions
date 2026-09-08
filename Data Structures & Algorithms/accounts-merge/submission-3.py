class UnionFind:
    def __init__(self, n):
        self.parent, self.rank = {}, {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)

        if par1 == par2:
            return
        
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2
        else:
            self.parent[par1] = par2
            self.rank[par2] +=1
        return

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(accounts))
        emailMap = {}

        for index, a in enumerate(accounts):
            for email in a[1:]:
                if email not in emailMap:
                    emailMap[email] = index
                else:
                    unionFind.union(index, emailMap[email])
        
        emailList = defaultdict(list)

        for email, index in emailMap.items():
            ind = unionFind.find(index)
            emailList[ind].append(email)
        
        result = []
        for index, email in emailList.items():
            name = accounts[index][0]
            result.append([name] + email)
        
        return result

        