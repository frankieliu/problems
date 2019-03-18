
My 1 line Python solution

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39571

* Lang:    python3
* Author:  xcv58
* Votes:   10

The logic is pretty straight, we find all peaks and related bottom elements, then sum all peaks minus all bottoms.


    class Solution:
        # @param prices, a list of integer
        # @return an integer
        def maxProfit(self, prices):
            return sum([y for x, y, z in zip(prices[0:-1], prices[1:], prices[2:] + [prices[-1]]) if y > x and y >= z]) - sum([y for x, y, z in zip([prices[0]] + prices[0:-2], prices[0:-1], prices[1:]) if y <= x and y < z]) if len(prices) > 0 else 0


UPDATE:

this version is more clear and simpler.

    class Solution:
        # @param prices, a list of integer
        # @return an integer
        def maxProfit(self, prices):
            return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])
