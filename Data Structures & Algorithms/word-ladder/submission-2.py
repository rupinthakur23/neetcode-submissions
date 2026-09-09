class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        
        adjaencyList = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                adjaencyList[pattern].append(word)
        q = deque([beginWord])
        visited = set([beginWord])
        
        turn = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return turn
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in adjaencyList[pattern]:
   
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            turn +=1
        
        return 0
        