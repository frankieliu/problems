
Python easy to understand solution.

https://leetcode.com/problems/count-primes/discuss/57587

* Lang:    python3
* Author:  caikehe
* Votes:   28

        
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)
