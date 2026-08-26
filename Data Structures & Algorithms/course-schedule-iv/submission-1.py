class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacencyList = defaultdict(list)

        for u, v in prerequisites:
            adjacencyList[v].append(u)
        
        courseMap = {}

        def dfs(course):
            if course not in courseMap:
                courseMap[course] = set()
            
                for preReq in adjacencyList[course]:
                    courseMap[course] |= dfs(preReq)
                
                courseMap[course].add(course)

            return courseMap[course]

        for course in range(numCourses):
            dfs(course)
        
        result = []

        for u,v in queries:
            result.append(u in courseMap[v])
        
        return result