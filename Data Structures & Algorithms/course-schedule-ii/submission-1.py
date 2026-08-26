class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}

        for dr, ds in prerequisites:
            courseMap[dr].append(ds)

        visited = set()

        result = []

        def bfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nextCourse in courseMap[course]:
                if not bfs(nextCourse):
                    return False

            if course not in result:
                result.append(course)
            visited.remove(course)
            courseMap[course] = []
            return True
                

        for course in range(numCourses):
            if not bfs(course):
                return []
        
        return result