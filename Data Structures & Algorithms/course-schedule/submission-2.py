class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}

        for cc, nc in prerequisites:
            courseMap[cc].append(nc)
        
        visited = set()
        
        def dfs(currCourse):
            if currCourse in visited:
                return False
            
            if courseMap[currCourse] == []:
                return True
            
            visited.add(currCourse)

            for courseNeeded in courseMap[currCourse]:
                if not dfs(courseNeeded):
                    return False
            
            visited.remove(currCourse)
            courseMap[currCourse] = []
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True