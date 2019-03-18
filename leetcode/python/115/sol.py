
Python dp solutions (O(m*n), O(n) space).

https://leetcode.com/problems/distinct-subsequences/discuss/37322

* Lang:    python3
* Author:  caikehe
* Votes:   9

    
    # O(m*n) space 
    def numDistinct1(self, s, t):
        l1, l2 = len(s)+1, len(t)+1
        dp = [[1] * l2 for _ in xrange(l1)]
        for j in xrange(1, l2):
            dp[0][j] = 0
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
        return dp[-1][-1]
      
    # O(n) space  
    def numDistinct(self, s, t):
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in xrange(1, l1):
            pre = cur[:]
            for j in xrange(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]
