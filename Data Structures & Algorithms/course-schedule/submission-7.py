class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adaencyList = defaultdict(list)

        for u, v in prerequisites:
            adaencyList[u].append(v)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for nei in adaencyList[course]:
                if not dfs(nei):
                    return False 

            visited.remove(course)
            adaencyList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True