class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)) + '#' + word)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        outputWord = ''

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return result

            

