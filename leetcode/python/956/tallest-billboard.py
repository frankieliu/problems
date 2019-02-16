"""956. Tallest Billboard
Hard

98

5

Favorite

Share

You are installing a billboard and want it to have the largest height.
The billboard will have two steel supports, one on each side.  Each
steel support must be an equal height.

You have a collection of rods which can be welded together.  For
example, if you have rods of lengths 1, 2, and 3, you can weld them
together to make a support of length 6.

Return the largest possible height of your billboard installation.  If
you cannot support the billboard, return 0.

Example 1:
Input: [1,2,3,6]
Output: 6

Explanation: We have two disjoint subsets {1,2,3} and {6}, which have
the same sum = 6.

Example 2:
Input: [1,2,3,4,5,6]
Output: 10

Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which
have the same sum = 10.

Example 3:
Input: [1,2]
Output: 0

Explanation: The billboard cannot be supported, so we return 0.

Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.
Accepted
2,230
Submissions
6,203

"""

class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """

        maxs = sum(rods) // 2
        dp = [0] * maxs + 1
        for el in dp:
            el = {}

        dp[0][tuple(rods)] = 1

        # dp collects the number of ways of reaching
        for n in range(1, maxs+1):
            for r in rods:
                if n-r >= 0:
                    dp[n] += dp[n-r]
        return dp


s = Solution()
print(s.tallestBillboard([1, 2, 3, 6]))

"""
Input: [1,2,3,6]
Output: 6
 dp[6][6][{1,2,3,6}] =
 dp[0][6][{1,2,3}] =
 dp[0][3][{1,2}]

 ...


 dp[10][10][{1,2,
 dp[10][{1,2,3}] = 0 < sum({1,2,3})
 dp[5][{1,2,3}] = 1
 dp[3][{1,2,2}] = 2

 dp[10][{1,2,3,5,6,7,8}] = 0 < sum({1,2,3})
 dp[9][{2,3,5,6,7,8}] +
 dp[8][{1,3,5,6,7,8}] +

 {1,2,3} -> hash

 dp[n][ ... ] = number of ways of reaching [n] given [ set of rods remaining ]

dp[n][{1,2,3}] = dp[n-1][{2,3}] + dp[n-2][{1,3}] + ...
                 dp[n-3][{1,2}]

how many ways to read step n
dp[n] = dp[n-1] + dp[n-3]
dp[n-1] = dp[n-2] + dp[n-4]

o(maxsum * num_of_rods)
sum"""
