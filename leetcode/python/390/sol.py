
Simple-minded python solution (illustrative only)

https://leetcode.com/problems/elimination-game/discuss/87125

* Lang:    python3
* Author:  ken.hsieh.2000@gmail.com
* Votes:   1

This is my dumb verification function to make sure I understand the Josephus problem-like recursion.  Hope it helps people that may come across it.

"""

    def helper(self, x):
        # uncomment this to see the input
        # print(x)

        # trivial return
        if len(x)==1: return x

        # take every other element and then reverse the list
        y = x[1:len(x):2]
        y.reverse()

        # recurse
        return self.helper(y)

    def lastRemaining(self, n):
        # for illustrative purpose only,
        # manipulate the list until only one element remains
        nums = range(1,n+1)
        return (self.helper(nums)[0])
"""
