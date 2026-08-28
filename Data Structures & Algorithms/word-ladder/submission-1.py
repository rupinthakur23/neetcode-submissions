class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wordMap = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                wordMap[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in wordMap[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            result +=1
        
        return 0






        