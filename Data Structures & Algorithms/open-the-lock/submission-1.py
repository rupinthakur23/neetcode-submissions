class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return - 1
        
        queue = deque(['0000'])
        visited = set(deadends)
        visited.add('0000')

        steps = 0

        while queue:
            for i in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return steps
                
                for i in range(len(lock)):
                    for j in [1, -1]:
                        lockCode =  str((int(lock[i]) + j + 10)%10)
                        newCode = lock[:i] + lockCode + lock[i + 1:]
                        if newCode in visited:
                            continue
                        print(newCode)
                        visited.add(newCode)
                        queue.append(newCode)
            steps +=1
        
        return -1


