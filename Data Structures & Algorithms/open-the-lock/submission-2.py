class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return - 1
        
        q = deque(['0000'])
        visited = set(deadends)
        visited.add('0000')
        attempts = 0

        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return attempts
                for i in range(len(lock)):
                    for j in [1, -1]:
                        lockCode = str((int(lock[i]) + j + 10)%10)
                        newCode = lock[:i] + lockCode + lock[i + 1:]

                        if newCode in visited:
                            continue
                        visited.add(newCode)
                        q.append(newCode)
            attempts +=1
        return -1
