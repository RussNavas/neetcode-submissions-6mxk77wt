class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 #buy day, sell day
        maxP = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell # we found a cheaper buy price
            sell += 1
        return maxP