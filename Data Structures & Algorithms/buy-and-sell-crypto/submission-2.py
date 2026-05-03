'''
[3,2,9,1,7,10]
''' 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        l, r = 0, 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            mp = max(mp, curProfit)
            if curProfit >= 0:
                r += 1
            else:
                l += 1
        
        return mp



