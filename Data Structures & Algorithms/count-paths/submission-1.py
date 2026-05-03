class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1

        if n > m:
            m, n = n, m

        
        res = j = 1

        for i in range(m, m + n - 1):
            res *= i
            res //= j

            j += 1

        return res
        
