class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ajcaencyList = defaultdict(list)
        for uv, uw in prerequisites:
            ajcaencyList[uv].append(uw)
        
        visited = set()
        result = []

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for nei in ajcaencyList[course]:
                if not dfs(nei):
                    return False

            if course not in result:
                result.append(course)
                
            visited.remove(course)
            ajcaencyList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result