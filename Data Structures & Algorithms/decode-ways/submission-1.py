'''
Questions:
- 29 wouldn't be invalid
- 0... wouldn't either
- Emty strings?

Intuition: Feels like a problem that can be expressed as an aggregation on a subproblem

f("1112") = 'A' + f(n-1), 'K' + f(n-2))

Recursive: O(2^N)

Bottom up dynamic programming: O(N)
Space: O(2N)


'''

class Solution:
    def numDecodings(self, s: str) -> int:
        db = [ None for c in s ]

        N = len(s)

        def isValid(sub):
            if len(sub) == 2:
                return int(sub[0]) > 0 and int(sub) <= 26

            return int(sub[0]) > 0


        def topDown(i):
            if i >= N:
                return 1

            if db[i]:
                return db[i]

            if i == N - 1:
                if isValid(s[i:]):
                    db[i] = 1
                else:
                    db[i] = 0

                return db[i]
                    
            
            res = 0

            if isValid(s[i: i+1]):
                res += topDown(i + 1)

            if isValid(s[i: i+2]):
                res += topDown(i + 2)

            db[i] = res
            return db[i]

        sol =  topDown(0)
        return sol

        