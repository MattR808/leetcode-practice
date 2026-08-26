class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max_profit = 0
        for price in prices:

            if buy > price:
                buy = price
            else:
                profit = price - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit
