class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        countOrder = {}
        for index, char in enumerate(order):
            countOrder[char] = index
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                
                if word1[j] != word2[j]:
                    if countOrder[word1[j]] > countOrder[word2[j]]:
                        return False
                    else:
                        break
        
        return True
