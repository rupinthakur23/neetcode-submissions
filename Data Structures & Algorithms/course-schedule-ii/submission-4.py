class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjaencyList = defaultdict(list)

        for uv, uw in prerequisites:
            adjaencyList[uv].append(uw)
        
        visited = set()
        traversed = set()

        result = []

        def dfs(course):
            if course in visited:
                return False
            
            if course in traversed:
                return True
            
            visited.add(course)

            for nextCourse in adjaencyList[course]:
                if not dfs(nextCourse):
                    return False
            
            visited.remove(course)
            traversed.add(course)
            result.append(course)

            adjaencyList[course] = []

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result