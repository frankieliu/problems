
Python DP solution 32ms, bottom-up, with explanation

https://leetcode.com/problems/predict-the-winner/discuss/96833

* Lang:    python3
* Author:  vinhhoang
* Votes:   4

```
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2 == 0 or len(nums) == 1:
            return True

        n = len(nums)
        dp = [[[0,0] for row in xrange(n)] for _ in xrange(n)]
        
        # bottom up, build each case starting from problem with 1 number in a game:
        # base case: only 1 number, player 1 pick first, player 2 will be left with 0 number game, aka 0
        # each dp[i][j] will store [bestScore, leftOver]
        for i in range(n):
            dp[i][i] = [nums[i], 0]
        
        # sub divide the game into list from index i to j 
        # now start from 2 number game [i][j]:
        # if player 1 pick i, player 2 will pick the bestScore of game [i+1][j], then player 1 is left with the leftOver of game [i+1][j]
        # if player 1 pick j, player 2 will pick the bestScore of game [i][j-1], then player 1 is left with the leftOver of game [i][j-1]
        # player 1 will choose the best case in above scenarios

        for length in xrange(2,n+1):
            for i in range(n-length+1):
                j = i + length-1
                # pick i:
                pi = dp[i+1][j][1] + nums[i]
                # pick j:
                pj = dp[i][j-1][1] + nums[j]
                if pi > pj:
                    dp[i][j][0] = pi
                    dp[i][j][1] = dp[i+1][j][0]

                else:
                    dp[i][j][0] = pj
                    dp[i][j][1] = dp[i][j-1][0]

        return dp[0][-1][0] >= dp[0][-1][1]
```
