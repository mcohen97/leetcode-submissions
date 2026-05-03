class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charPositions = {}
        maxLength = 0

        l = r = 0

        while r < len(s):
            currentChar = s[r]
            if currentChar in charPositions and charPositions[currentChar] >= l:
                repeatedCharPos = charPositions[currentChar]
                l = repeatedCharPos + 1
                charPositions[currentChar] = r
            else:
                charPositions[currentChar] = r
                maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength


        
        