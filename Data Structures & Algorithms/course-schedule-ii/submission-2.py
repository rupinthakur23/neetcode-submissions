class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}

        for dr, ds in prerequisites:
            courseMap[dr].append(ds)

        visited = set()
        cycle = set()

        result = []

        def bfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True
            
            cycle.add(course)

            for nextCourse in courseMap[course]:
                if not bfs(nextCourse):
                    return False

            visited.add(course)
            cycle.remove(course)
            result.append(course)
            return True
                

        for course in range(numCourses):
            if not bfs(course):
                return []
        
        return result