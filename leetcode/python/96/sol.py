
Python solutions (DP + Catalan number)

https://leetcode.com/problems/unique-binary-search-trees/discuss/31826

* Lang:    python3
* Author:  caikehe
* Votes:   28

   
    # DP
    def numTrees1(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
     
    # Catalan Number  (2n)!/((n+1)!*n!)  
    def numTrees(self, n):
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
