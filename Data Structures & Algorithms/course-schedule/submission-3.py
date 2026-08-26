class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        completed = set()

        for dr, ds in prerequisites:
            courseMap[dr].append(ds)
        
        def dfs(startingCouse):
            if startingCouse in completed:
                return False
            
            if courseMap[startingCouse] == []:
                return True

            completed.add(startingCouse)

            
            for course in courseMap[startingCouse]:
                if not dfs(course):
                    return False
            
            courseMap[startingCouse] = []
            completed.remove(startingCouse)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True