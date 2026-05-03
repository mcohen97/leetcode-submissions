class Solution:
    endChar = '#'

    def encode(self, strs: List[str]) -> str:
        encoded  = ''
        for word in strs:
            fullBlocks = len(word) // 9
            lastBlockLength = len(word) % 9
            for i in range(fullBlocks):
                encoded += '9' + word[i * 9: (i + 1) * 9]
            encoded +=  str(lastBlockLength) + word[len(word) - lastBlockLength: ] + self.endChar
        return encoded
        
           


    def decode(self, s: str) -> List[str]:
        i = 0
        solution = []

        while i < len(s):
            currentWord = ''
            while s[i] != self.endChar:
                currentBlockLength = int(s[i])
                currentWord += s[i + 1: i + 1 + currentBlockLength]
                i += 1 + currentBlockLength
            solution.append(currentWord)
            i += 1
        return solution

       
        



        
