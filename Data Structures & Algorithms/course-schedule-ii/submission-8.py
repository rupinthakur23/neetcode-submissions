class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        adaencyList = defaultdict(list)

        for u, v in prerequisites:
            adaencyList[u].append(v)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for nei in adaencyList[course]:
                if not dfs(nei):
                    return False 

            visited.remove(course)
            adaencyList[course] = []
            if course not in result:
                result.append(course)
                
        
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return list(result)