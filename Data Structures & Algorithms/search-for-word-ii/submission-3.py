class Trie:
    def __init__(self):
        self.children = {}
        self.found = False

class TrieNode:
    def __init__(self):
        self.root = Trie()
    
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char] 
        curr.found = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        ROWS, COLS = len(board), len(board[0])

        visited, result = set(), set()

        def dfs(r, c, node, word):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or  board[r][c] not in node.children:
                return False
            
            word += board[r][c] 
            node = node.children[board[r][c]]

            if node.found:
                result.add(word)
            
            visited.add((r,c))

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

            return 

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j, trie.root, '')
        
        return list(result)
        
        