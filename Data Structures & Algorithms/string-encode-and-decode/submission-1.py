class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []
        for word in strs:
            encodedString.append(str(len(word)))
            encodedString.append('#')
            encodedString.append(word)
        return ''.join(encodedString)


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j +=1
            
            length = int(s[i:j])
            result.append(s[j + 1 : j + length + 1])
            i =  j + length + 1

            
        
        return result

