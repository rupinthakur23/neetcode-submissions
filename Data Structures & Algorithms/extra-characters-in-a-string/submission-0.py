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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)
        
        dp = {len(s) : 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            curr = trie.root
            res = 1 + dfs(i + 1)

            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.found:
                    res = min(res, dp[j + 1])
            
            dp[i] = res
            return res

        return dfs(0)
        