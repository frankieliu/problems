
Easy O(n) Python solution

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39049

* Lang:    python3
* Author:  girikuncoro
* Votes:   94

    def maxProfit(prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
