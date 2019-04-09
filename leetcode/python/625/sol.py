
Short math solution for C++ & Python

https://leetcode.com/problems/minimum-factorization/discuss/104680

* Lang:    python3
* Author:  zqfan
* Votes:   0

C++ solution
```
class Solution {
public:
    int smallestFactorization(int a) {
        if ( a < 10 )
            return a;
        long b = 0;
        for ( int i = 0; i < 11 && a != 1; ++i ) {
            for ( int d = 9; d > 1; --d ) {
                if ( a % d == 0 ) {
                    b += pow(10, i) * d;
                    a /= d;
                    break;
                }
            }
        }
        return ( b > INT_MAX || a != 1 ) ? 0 : b;
    }
};
```
Python solution
```
class Solution(object):
    def smallestFactorization(self, a):
        if a < 10:
            return a
        b = 0
        for i in xrange(11):
            for d in xrange(9, 1, -1):
                if a % d == 0:
                    b += (10 ** i) * d
                    a /= d
                    break
        return b if b < (1 << 31) and a == 1 else 0
```
