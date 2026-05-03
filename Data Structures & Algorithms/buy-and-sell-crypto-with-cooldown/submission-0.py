class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def maxProfitRec(i, bought): 
            if i >= len(prices):
                return 0

            if (i, bought) in dp:
                return dp[(i, bought)]
            
            if bought:
                dp[(i, bought)] =  max(prices[i] + maxProfitRec(i + 2, False), maxProfitRec(i + 1, True))
            else:
                dp[(i, bought)] =  max(-prices[i] + maxProfitRec(i + 1, True), maxProfitRec(i + 1, False))

            return dp[(i, bought)]

        maxProfitRec(0, False)
        return dp[(0, False)]        