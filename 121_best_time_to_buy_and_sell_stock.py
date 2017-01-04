"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""
import sys

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        min_former, max_latter = [0]*(n-1), [0]*(n-1)
        min_former[0] = prices[0]
        max_latter[-1] = prices[-1]
        max_profile = 0
        for i in range(1, n-1):
            min_former[i] = min(prices[i], min_former[i-1])
        for i in range(n-3, -1, -1):
            max_latter[i] = max(prices[i+1], max_latter[i+1])
        for i in range(n-1):
            if max_latter[i] - min_former[i] > max_profile:
                max_profile = max_latter[i] - min_former[i]
        return max_profile

    def maxProfit2(self, prices):
        min_price = sys.maxsize
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit
