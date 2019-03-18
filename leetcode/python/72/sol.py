
Python solutions (O(m*n), O(n) space).

https://leetcode.com/problems/edit-distance/discuss/25879

* Lang:    python3
* Author:  caikehe
* Votes:   14

        
   

    
    # O(m*n) space
    def minDistance1(self, word1, word2):
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in xrange(l2)] for _ in xrange(l1)]
        for i in xrange(l1):
            dp[i][0] = i
        for j in xrange(l2):
            dp[0][j] = j
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
                    
    
    # O(n) space with rolling array            
    def minDistance(self, word1, word2):
        l1, l2 = len(word1)+1, len(word2)+1
        pre = [0 for _ in xrange(l2)]
        for j in xrange(l2):
            pre[j] = j
        for i in xrange(1, l1):
            cur = [i]*l2
            for j in xrange(1, l2):
                cur[j] = min(cur[j-1]+1, pre[j]+1, pre[j-1]+(word1[i-1]!=word2[j-1]))
            pre = cur[:]
        return pre[-1]
