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
        root = Trie()
        result, visited = set(), set()
        for word in words:
            root.addWord(word)
        
        
        def dfs(r, c, node, word):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] not in node.children:
                return
    
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.found:
                result.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root.root, '')
        return list(result)












        