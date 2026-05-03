'''
Intuition:

Starting small.
If there's only one step, then one combination: 1
If there's 2 steps, then 2 possibilities, 1 twice or 2 once.
If it's 3 steps. 
Since we are choosing one step at a time, and there's a similar problem after that, and a base case
We can solve this with dynamic programming.

climb(1) = 1
climb(0) = 1

climb(2) = climb(1) + climb(0)

climb(n) = climb(n-1) + climb(n-2)

O(2^N) -> recursively with no Memory cache
O(N) -> iteratively using bottom up DP
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        nMinus2 = 1
        nMinus1 = 1

        if n == 1:
            return nMinus1
        
        for i in range(1, n):
            cur = nMinus1 + nMinus2
            nMinus2 = nMinus1
            nMinus1 = cur
        
        return cur
            
        



        