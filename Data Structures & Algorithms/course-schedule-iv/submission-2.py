class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjaencyList = defaultdict(list)
        for uv, uw in prerequisites:
            adjaencyList[uw].append(uv)
        
        courseMap = {}
        def dfs(course):
            if course not in courseMap:
                courseMap[course] = set()
            
                for nei in adjaencyList[course]:
                    courseMap[course] |= dfs(nei)
                courseMap[course].add(course)
            
            return courseMap[course]
            
        for i in range(numCourses):
            dfs(i)

        result = [False] * len(queries)

        for index, value in enumerate(queries):
            if value[0] in courseMap[value[1]]:
                result[index] = True
        
        return result

