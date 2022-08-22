# greedy 알고리즘
class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_day = prices[0]
        
        for x in prices:
            profit = max(profit, x - min_day)
            min_day = min(min_day, x)
        return profit