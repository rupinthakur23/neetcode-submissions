class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []

        if dst not in self.graph:
            self.graph[dst] = []
        
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        
        self.graph[src].remove(dst)
        return True
        
        return False
    
    def hasPathDfs(self,src, dst, visited):
        if src == dst:
            return True
        
        visited.add(src)

        for neighbour in self.graph[src]:
            if neighbour not in visited:
                if self.hasPathDfs(neighbour, dst, visited):
                    return True
        
        return False
        
 
    def hasPath(self, src: int, dst: int) -> bool:
        return self.hasPathDfs(src, dst, set())



