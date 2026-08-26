class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coueseMap = { i:[] for i in range(numCourses)}

        for dr, ds in prerequisites:
            coueseMap[dr].append(ds)
        
        visited = set()

        def bfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nextCourse in coueseMap[course]:
                if not bfs(nextCourse):
                    return False
            
            visited.remove(course)
            coueseMap[course] = []

            return True


        for course in range(numCourses):
            if not bfs(course):
                return False
        
        return True