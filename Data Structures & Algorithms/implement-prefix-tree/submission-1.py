class Trie:
    def __init__(self):
        self.children = {}
        self.isFound = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char] 
        curr.isFound = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char] 
        return curr.isFound
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char] 
        return True
        
        