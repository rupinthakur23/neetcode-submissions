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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            root.addWord(word)

        dp = {len(s) : 0}

        result = 0

        def dfs(i):
            if i in dp:
                return dp[i]
            curr = root.root
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



        