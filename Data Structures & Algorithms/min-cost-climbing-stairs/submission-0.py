'''
f(n) = cost[n]
f(n-1) = cost[n - 1]

f(0) = cost[0] + min(f(1), f(2))

O(2^N)
O(N)

Space O(1)

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2], cost[-1]
        N = len(cost)

        for i in range(N - 3, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)
        

          






        