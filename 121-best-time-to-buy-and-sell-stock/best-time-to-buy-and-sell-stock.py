class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=1
        best=0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                best = max(best, profit)
            else:
                buy=sell
            sell+=1
        return best


        