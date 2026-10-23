class Trie:
    def __init__(self):
        self.children = {}
        self.found = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char] 
        curr.found = True
        
    def search(self, word: str) -> bool:
        def dfs(i, curr):
            
            for j in range(i, len(word)):
                if word[j] == '.':
                    for char in curr.children.values():
                        if dfs(j + 1, char):
                            return True
                    return False

                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]] 
            return curr.found

        return dfs(0, curr = self.root)
        
