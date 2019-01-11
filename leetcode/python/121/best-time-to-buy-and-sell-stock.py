"""121. Best Time to Buy and Sell Stock
Easy

1973

101

Favorite

Share

Say you have an array for which the ith element is the price of a
given stock on day i.

If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0

Explanation: In this case, no transaction is done, i.e. max profit = 0.
Accepted
403,057
Submissions
886,693
"""
class Solution:

    def maxRunningSum(self, a):
        amax_begin = -1
        amax_end = -1
        amax = 0

        curr_begin = -1
        curr_sum = 0

        for i in range(0, len(a)):
            el = a[i]
            if el > curr_sum + el:
                curr_begin = i
                curr_sum = el
            else:
                curr_end = i
                curr_sum = curr_sum + el

            if curr_sum > amax:
                amax = curr_sum
                amax_begin = curr_begin
                amax_end = curr_end

        return (amax, amax_begin, amax_end)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        delta = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        # each index represents the difference between two prices
        # if we want to encompass the equivalent range then we need
        # to add an additional 1 to the ending index:
        #
        # e.g.
        # deltas:
        # 0     1     2
        # (0-1) (1-2) (2-3)  ...
        #
        # For delta index 1 to 2 the equivalent price index is 1 to 3
        a = self.maxRunningSum(delta)
        return a[0]


s = Solution()
s.maxProfit([7,1,5,3,6,4])
