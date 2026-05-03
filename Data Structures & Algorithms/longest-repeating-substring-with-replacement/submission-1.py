class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        counts = {}

        l = r = 0

        while r < len(s):
            curr = s[r]
            counts[curr] = counts.get(curr, 0) + 1
            curLength = r - l + 1
            mostCommonChar = max(counts, key = counts.get)
            if curLength - counts[mostCommonChar] > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1
            else:
                result = max(result, curLength)
            
            r += 1
        
        return result

            
                

            

