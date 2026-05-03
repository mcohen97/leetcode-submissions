class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowCounter = {}
        tCounter = Counter(t)
        tCharCount = len(tCounter)
        matches = 0
        sol = ""

        l = r = 0

        while r < len(s):
            char = s[r]
            windowCounter[char] = windowCounter.get(char ,0) + 1

            if windowCounter[char] == tCounter[char]:
                matches += 1


            while matches == tCharCount:
                if not sol or r - l + 1 < len(sol):
                    sol = s[l: r+1]
                char = s[l]

                windowCounter[char] = windowCounter[char] - 1

                if windowCounter[char] == tCounter[char] - 1:
                    matches -= 1
                    
                l += 1


            r += 1
                
        return sol
        
        