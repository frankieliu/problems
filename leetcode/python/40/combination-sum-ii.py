"""40. Combination Sum II
Medium

639

34

Favorite

Share

Given a collection of candidate numbers (candidates) and a target
number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.

The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,

A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,

A solution set is:
[
  [1,2,2],
  [5]
]

Accepted
190,527
Submissions
484,863

"""
class Solution:
    def combinationSum2(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        h = {}
        for x in c:
            if x not in h:
                h[x] = 1
            else:
                h[x] += 1
        cset = list(h.keys())

        dp = [0] * (t+1)
        for i in range(1, t+1):
            dp[i] = [0] * len(cset)
        dp[0] = [1] * len(cset)

        for i in range(0, len(cset)):
            for tt in range(0, t+1):
                sum = 0
                for j in range(0, h[cset[i]]+1):
                    if tt - j * cset[i] >= 0:
                        sum += dp[tt-j*cset[i]][i-1]
                        # print(tt, cset[i], tt-j*cset[i])
                dp[tt][i] = sum

        # return dp[t][len(cset)-1]
        return dfs(dp, t, h, cset, len(cset)-1)


# h keeps count
# i tells which one to keep
def dfs(dp, tt, h, c, i):
    if tt == 0:
        return [[]]
    if tt < 0 or i < 0 or dp[tt][i] <= 0:
        return []

    ssol = []
    # consider all possible answers
    for j in range(0, h[c[i]] + 1):
        sol = [x + [c[i]]*j for x in dfs(dp, tt - j*c[i], h, c, i-1)]
        ssol += sol

    return ssol


s = Solution()
print(s.combinationSum2([2,5,2,1,2,2,2,2,2,2,2], 5))
