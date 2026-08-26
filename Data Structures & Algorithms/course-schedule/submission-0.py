class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}

        for dr, ds in prerequisites:
            courseMap[dr].append(ds)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if not courseMap[crs]:
                return True
            
            visited.add(crs)

            for prerequisites in courseMap[crs]:
                if not dfs(prerequisites):
                    return False
            

            visited.remove(crs)
            courseMap[crs] = []
            return True
        
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        
        return True
