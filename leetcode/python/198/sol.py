
Python DP solution, 4 line, O(n) time, O(1) space, easy to understand with detailed explanation

https://leetcode.com/problems/house-robber/discuss/55977

* Lang:    python3
* Author:  cjhuo
* Votes:   24

The idea is the store the max sum we can get for each house use it to calculate the following houses until we get the final result.

In the path that the robber chose to rob with max money, it is guaranteed that either the last house (num[-1]) or the 2nd last house (num[-2]) will be robbed. So we can compare the max sum path that includes num[-1] with the max sum path that includes num[-2] and return the larger one.

To get the sums of the two paths, we scan from left to right. A sliding window of size 4, `[max_3_house_before, max_2_house_before, adjacent, cur]`, is used to calculate the max sum till the current house. The last element, `cur`, of the window is the money of the current house we are scanning. The 1st element, `max_3_house_before`, stores the max sum till the house that is 3 steps before the current one. The 2nd element, `max_2_house_before`, stores the max sum till the house that is 2 steps before the current one. The 3rd element, `adjacent`, stores the max sum till the house that are one step before the current one. To reach the current house, we either came from the house that is 3 steps before or from the one that is 2 steps before because visiting two adjacent houses is not allowed. So we can get the max sum till the current house by `max(cur+max_3_house_before, cur+max_2_house_before)`. 

Before scanning the next house we update the window by moving one house forward: `max_3_house_before, max_2_house_before, adjacent = max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)`.

When we finished the scanning, the max sum exists in either `max_2_house_before` or `adjacent`. So we return `max(max_2_house_before, adjacent)`.

For example: `num = [1,7,9,4]`, at the beginning,  `max_3_house_before, max_2_house_before, adjacent` are initialized to 0, so it is like putting 3 zeros before the input list `[0, 0, 0, 1, 7, 9, 4]`. Here are steps for calculating the max sum for each house(the sliding window is marked by parentheses):

> [(0, 0, 0, **1**), 7, 9, 4], cur = max(0+1, 0+1)

> -> [ (0, 0, 1, **7**), 9, 4], cur = max(0+7, 0+7)

> -> [(0, 1, 7, **9**), 4], cur =  max(0+9, 1+9)

> -> [(1, 7, 10, **4**)], cur = max(1+4, 7+4)

> -> [7, 10, 11],  10 is the max sum of path that includes num[-2], 11 is the max sum of path that includes num[-1], so return max(10, 11)

Code:

        class Solution:
            # @param num, a list of integer
            # @return an integer
            def rob(self, num):
                max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
                for cur in num:
                    max_3_house_before, max_2_house_before, adjacent = \\
                    max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
                return max(max_2_house_before, adjacent)

There is a better solution using only 2 variables [here][1] but I found out myself too dumb and was able to understand it after I stared at it for 30min:(


  [1]: https://leetcode.com/discuss/30102/4-line-python-o-1-space-o-n-time-with-explaination-simplest
