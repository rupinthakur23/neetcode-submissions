class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ajcaencyList = defaultdict(list)
        for uv, uw in prerequisites:
            ajcaencyList[uv].append(uw)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nei in ajcaencyList[course]:
                if not dfs(nei):
                    return False
                
            visited.remove(course)
            ajcaencyList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True