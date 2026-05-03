class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsCounts = {}

        for char in s:
            charsCounts[char] = charsCounts.get(char, 0) + 1
        
        for char in t:
            if charsCounts.get(char, 0) <= 0:
                return False
            
            charsCounts[char] = charsCounts.get(char, 0) - 1

            if charsCounts.get(char, 0) <= 0:
                del charsCounts[char]

        return len(charsCounts) == 0