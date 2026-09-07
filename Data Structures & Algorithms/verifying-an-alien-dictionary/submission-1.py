class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}

        for index, char in enumerate(order):
            orderMap[char] = index
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                if word1[j] != word2[j]:
                    if orderMap[word1[j]] < orderMap[word2[j]]:
                        break
                    else:
                        return False
        return True