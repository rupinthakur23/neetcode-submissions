class TrieNode:
    def __init__(self):
        self.children = {}
        self.found = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.found = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        curr = Trie()
        result = set()
        visited = set()

        for word in words:
            curr.addWord(word)       
        
        def dfs(r, c, start, currWord):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] not in start.children:
                return
            
            visited.add((r,c))

            start = start.children[board[r][c]]

            currWord += board[r][c]
            if start.found:
                result.add(currWord)

            dfs(r + 1, c, start, currWord)
            dfs(r, c + 1, start, currWord)
            dfs(r - 1, c, start, currWord)
            dfs(r, c - 1, start, currWord)

            visited.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, curr.root, "")
        
        return list(result)
        