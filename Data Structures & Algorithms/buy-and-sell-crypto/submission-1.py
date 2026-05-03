class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ws = we = 0
        maxP = 0

        while we < len(prices):
            curr = prices[we] - prices[ws]

            if prices[we] >= prices[ws]:
                we += 1
            else:
                ws = we
            
            maxP = max(maxP, curr)

        return maxP
        
        
