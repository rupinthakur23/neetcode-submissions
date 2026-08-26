class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjaencyList = defaultdict(list)

        for uv, uw in prerequisites:
            adjaencyList[uv].append(uw)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nextCourse in adjaencyList[course]:
                if not dfs(nextCourse):
                    return False
            
            visited.remove(course)
            adjaencyList[course] = []

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True