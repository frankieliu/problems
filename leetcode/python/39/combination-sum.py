"""39. Combination Sum
Medium

1521

43

Favorite

Share

Given a set of candidate numbers (candidates) (without duplicates) and
a target number (target), find all unique combinations in candidates
where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited
number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
Accepted
285,784
Submissions
627,425
"""

class Solution:
    def combinationSum(self, c, t):

        dp = [0] * (t+1)
        for i in range(0, t+1):
            dp[i] = [0] * len(c)
        dp[0] = [1] * len(c)

        for tt in range(1, t+1):
            # all the coin denominations
            # has to start with just one denomination
            # build up from that

            for i in range(0, len(c)):

                if tt >= c[i]:
                    a = dp[tt-c[i]][i]
                else:
                    a = 0
                if i >= 1:
                    # NOTE ith SOLUTION contains
                    # i, i-1, i-2, denominations
                    # This is our own definition
                    b = dp[tt][i-1]
                else:
                    b = 0

                dp[tt][i] = a + b

        # return dp[target][len(c)-1]

        """
        dp[target][i] comes from the summation of
        dp[target][i-1] and dp[target-c[i]][i]
        i.e solution without i,
        and the solution with i, with a coin removed
        """
        return self.dfs(c, dp, t, len(c)-1)

    def dfs(self, c, dp, tt, i):

        if tt == 0:
            return [[]]

        if i < 0 or tt < 0 or dp[tt][i] <= 0:
            return []

        "left: branch"
        left = []
        left = self.dfs(c, dp, tt, i-1)

        "right: branch"
        right = [x + [c[i]] for x in self.dfs(c, dp, tt-c[i], i)]
        return left + right


        # $2
        # [$1, [1,3]], [$2, [3]]
        # $4
        # [$3, [1,3]] + [$4, [3]]

s = Solution()
print(s.combinationSum([1, 3], 7))
